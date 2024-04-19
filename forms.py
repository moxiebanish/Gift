from django import forms
from .models import Wish


class EmailPostForm(forms.Form):
    Your_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"placeholder": "John Doe"}))
    Mpesa_No = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={"placeholder": "798******"}))
    Target_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={"placeholder": "John Doe"}))
    Target_email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"placeholder": "example@gmail.com"}))
    Target_No = forms.CharField(max_length=10, widget=forms.NumberInput(attrs={"placeholder": "798******",'type':'tel'}))


class WhatsappForm(forms.Form):
    Your_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Enter your Name"}))
    Your_mpesa_No = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "0756."}))
    Recipients_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Recipient's Name"}))
    Recipients_No = forms.CharField(max_length=50, widget=forms.NumberInput(attrs={"placeholder": "734******"}))


class WishForm(forms.ModelForm):
    Message = forms.CharField(max_length=300, label='', widget=forms.Textarea(attrs={"placeholder": "Write your wish here..."}))
    whatsapp = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    Gmail = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    class Meta:
        model = Wish
        fields = ['Message', 'whatsapp', 'Gmail']

