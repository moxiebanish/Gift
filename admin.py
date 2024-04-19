from django.contrib import admin
from .models import UploadedImage, TrackingModel, HomeImage, Reference,Talks
from django.utils.safestring import mark_safe
from django_daraja.models import AccessToken
from django.db.models import Avg

from django.http import HttpResponseRedirect
from django.urls import path


# Register your models here.
from django.contrib import admin

# Register your models here.



class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image_preview', 'upload_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="50"/>')

    image_preview.short_description = 'Image Preview'


admin.site.register(UploadedImage, UploadedImageAdmin)


class HomeImageAdmin(admin.ModelAdmin):
    list_display = ('description', 'image_preview', 'upload_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="50"/>')

    image_preview.short_description = 'Image Preview'


admin.site.register(HomeImage, HomeImageAdmin)


class TalksAdmin(admin.ModelAdmin):
    list_display = ('phone', 'key')


admin.site.register(Talks, TalksAdmin)


class TrackingModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailtrac', 'Sendspace')


admin.site.site_header = "GiftMe"
admin.site.register(TrackingModel, TrackingModelAdmin)


class AccesTokenAdmin(admin.ModelAdmin):
    list_display = ('token', 'created_at')


admin.site.register(AccessToken, AccesTokenAdmin)


class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('reference',)

admin.site.register(Reference, ReferenceAdmin)
