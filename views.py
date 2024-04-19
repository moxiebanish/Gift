from django.shortcuts import render, get_object_or_404, redirect
from .models import UploadedImage, TrackingModel, HomeImage, Reference, Talks
from .forms import WishForm, EmailPostForm, WhatsappForm
from django.core.mail import EmailMessage
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from .africastalkin import smsend
from .whatstalkin import talkwhatsapp
from django_pesapal.views import PaymentRequestMixin, TemplateView
from django.http import JsonResponse
import requests
from .saver import saver
import time
import random



def generate_reference_number():
    timestamp = int(time.time())  # Current timestamp
    random_number = random.randint(1000, 9999999)  # Random 4-digit number
    reference_number = int(f"{timestamp}{random_number}")
    return reference_number






super_numbers = [
    '+254757060626',
    '+254701235170',
    '+254102788034'
]
key='pk_live_cc322cb1cf1fab1c30f51e84f18e9449dbc28736'
class PaymentView(PaymentRequestMixin, TemplateView):

    def get_pesapal_payment_iframe(self):

        '''
        Authenticates with pesapal to get the payment iframe src
        '''
        order_info = {
            'first_name': 'Some',
            'last_name': 'User',
            'amount': 100,
            'description': 'Payment for X',
            'reference': 2,  # some object id
            'email': 'user@example.com',
        }

        iframe_src_url = self.get_payment_url(**order_info)
        return iframe_src_url
def index(request):
    cl = MpesaClient()
    phone_number = '254797530854'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://api.darajambili.com/express-payment'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    print(response)
    return HttpResponse(response)


def home(request):
    reference = request.POST.get('reference', '')
    image = HomeImage.objects.get(pk=3)
    header_image = HomeImage.objects.get(pk=1)
    xmas = HomeImage.objects.get(pk=4)
    NewYear = HomeImage.objects.get(pk=6)
    Valentine = HomeImage.objects.get(pk=2)
    Birthday = HomeImage.objects.get(pk=5)
    return render(request, 'coroute/home.html', {'image': image, 'header_image': header_image, 'xmas': xmas, 'NewYear': NewYear, 'Valentine': Valentine, 'Birthday': Birthday})

def about(request):
    return render(request, 'coroute/about.html')


def image_gallery(request):
    header_image = HomeImage.objects.get(pk=1)
    image = HomeImage.objects.get(pk=3)
    images = UploadedImage.objects.all()
    return render(request, 'coroute/gallery.html', {'images': images, "image": image, "header_image": header_image})


def image_detail(request, image_id):
    imageback = HomeImage.objects.get(pk=1)
    header_image = HomeImage.objects.get(pk=1)
    image = get_object_or_404(UploadedImage, pk=image_id)
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data['Message']
            wh = form.cleaned_data['whatsapp']
            gm = form.cleaned_data['Gmail']
            form.save(commit=False)
            if wh and not gm:
                return redirect('coroute:whatsapp', par1=cd, par2=image_id)
            elif gm and not wh:
                return redirect('coroute:mail', par1=cd, par2=image_id)
    else:
        form = WishForm()
    return render(request, 'coroute/detail.html',  {'form': form, 'image': image, 'imageback': imageback, 'header_image':header_image})


def maile(request, par1, par2):
    content = par1
    gift = par2
    sent = False
    header_image = HomeImage.objects.get(pk=1)
    image = get_object_or_404(UploadedImage, pk=gift)
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            index(request)
            cd = form.cleaned_data
            Email = cd['Target_email']
            username, domain = Email.split("@")
            userb = username[0:4]
            username_len = len(username)-4
            asterize = '*'*username_len
            Email= userb+asterize+"@"+domain
            subject = f" {cd['Your_name']} Wishes you a Merry Christmas "
            message = f"{content}"
            image_path = str(image.image.url[1:])
            filename = str(image.image.url[14:])
            image_data = open(image_path, 'rb').read()
            email = EmailMessage(subject, message, 'giftmejsm@gmail.com', [cd['Target_email']], )
            email.attach(filename=filename, content=image_data, mimetype='image/jpeg')
            name = form.cleaned_data['Your_name']
            phone = form.cleaned_data['Target_No']
            phone = '+254' + phone[1:]
            r_name = form.cleaned_data['Target_name']
            m_number = form.cleaned_data['Mpesa_No']
            email.send()
            sent = True
            if sent:

                index(request)
                Emails = TrackingModel(mailtrac="Email sent on", Sendspace=datetime.now())
                Emails.save()
                sent = f'Email sent Successfully to {Email}'
    else:
        form = EmailPostForm()
    return render(request, 'coroute/mail.html', { 'form': form, 'sent': sent, 'content': content, 'image': image, 'header_image':header_image})


def whatsapp(request, par1, par2):
    s_reference_number = generate_reference_number()
    content = par1
    gift = par2
    header_image = HomeImage.objects.get(pk=1)
    image = get_object_or_404(UploadedImage, pk=gift)
    if request.method == 'POST':
        s_reference_number = str(s_reference_number)
        form = WhatsappForm(request.POST)
        print(s_reference_number + 'yet')
        if form.is_valid():
            s_reference_number=s_reference_number
            image_url = str(image.mediaurl)
            name = form.cleaned_data['Your_name']
            phone = form.cleaned_data['Recipients_No']
            phone = '+254'+phone[1:]
            r_name = form.cleaned_data['Recipients_name']
            m_number = form.cleaned_data['Your_mpesa_No']
            m_number = '+254' + m_number[1:]
            concatinated_name = name+', '+r_name+' '+'('+f'{m_number}'+')'
            message = f'Dear {r_name}, {name} ({m_number}) has sent you {image.title} as a gift and the the following wish:\n {content}\n\nFollow the link below to wish your loved ones happy moments\n https://www.instagram.com/gift.mevirtualgifts?utm_source=qr&igshid=ZTM4ZDRiNzUwMw=='
            if message:
                if m_number in super_numbers:
                    smsend(message, phone)
                    talkwhatsapp(concatinated_name, content, phone, image_url)
                saver(concatinated_name, content, phone, image_url, message, s_reference_number)



    else:
        form = WhatsappForm()
    return render(request, 'coroute/app.html',  {'form': form, 'content': content, 'header_image': header_image,'image':image, 'key':key, "s_reference_number":s_reference_number})
# views.py


def verify_payment_status(request):
    if request.method == 'POST':
        reference = request.POST.get('reference')
        reference = reference
        print(reference + 'verified')
        if reference:
            talks_instance = Talks.objects.get(key=reference)
            smsend(talks_instance.message, talks_instance.phone)
            talkwhatsapp(talks_instance.concatinated_name, talks_instance.content, talks_instance.phone,
                         talks_instance.image_url)
            print(talks_instance.message)
            print(talks_instance.phone)
            print(talks_instance.concatenated_name)
            print(talks_instance.content)
            print(talks_instance.phone)
            print(talks_instance.image_url)
        paystack_secret_key = key
        paystack_verify_url = f'https://api.paystack.co/transaction/verify/{reference}'

        headers = {
            'Authorization': f'Bearer {paystack_secret_key}',
            'Content-Type': 'application/json',
        }

        try:
            # Send a request to Paystack to verify the payment
            response = requests.get(paystack_verify_url, headers=headers)
            data = response.json()
            if response.status_code == 200 and data.get('status') == True:

               # Payment was successful
               return JsonResponse({'status': 'success', 'message': 'Payment verification successful'})
            else:
                # Payment failed or verification unsuccessful
                return JsonResponse({'status': 'error', 'message': 'Payment verification failed'})

        except Exception as e:
            # Handle exceptions
            return JsonResponse({'status': 'error', 'message': f'Error verifying payment: {str(e)}'})

    # Handle invalid requests (GET requests)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
