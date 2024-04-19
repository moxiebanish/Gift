from django.db import transaction
from .models import Talks


def saver(concatinated_name, content, phone, image_url, message, s_reference_number):
    Talks(concatinated=concatinated_name, content=content, phone=phone,image=image_url,message=message, key=s_reference_number).save()
