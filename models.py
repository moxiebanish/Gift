from django.db import models
from ckeditor import fields


class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/', default=None)
    title = models.CharField(max_length=50, default=None)
    slug = models.SlugField(max_length=1000, unique_for_date='upload_date', default=None)
    upload_date = models.DateTimeField(auto_created=True, default=None)
    description = fields.RichTextField(blank=True, default=None)
    mediaurl = models.CharField(max_length=1000, default=None)
    urrls = models.CharField(max_length=1000, default=None)

    def __str__(self):
        return self.description


class HomeImage(models.Model):
    image = models.ImageField(upload_to='HomeImage/')
    title = models.CharField(max_length=50, default=None)
    slug = models.SlugField(max_length=50, default=None, unique_for_date='upload_date')
    upload_date = models.DateTimeField(auto_created=True, default=None)
    description = fields.RichTextField(blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.description
    class Meta:
        ordering = ("-pk",)


class Wish(models.Model):
    Message = models.CharField('wishful message',max_length=300)
    whatsapp = models.BooleanField(default=False)
    Gmail = models.BooleanField(default=False)


class TrackingModel(models.Model):
    mailtrac = models.CharField(max_length=50)
    Sendspace = models.DateTimeField(auto_now_add=True)


class Reference(models.Model):
    reference = models.CharField(max_length=80)


class Talks(models.Model):
    concatinated = models.CharField(max_length=300)
    content = models.CharField(max_length=3000)
    phone = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    message = models.CharField(max_length=500)
    key = models.CharField('Key Value', max_length=100)