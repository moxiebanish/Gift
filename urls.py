"""
URL configuration for GME project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import image_gallery, image_detail, maile, whatsapp, home, index, about, verify_payment_status
from django.conf import settings
from django.conf.urls.static import static


app_name = 'coroute'
urlpatterns = [
    path('index', index, name='index'),
    path('', home, name='home'),
    path('image_gallery/', image_gallery, name='image_gallery'),
    path('<int:image_id>/detail/', image_detail, name='image_detail'),
    path('<str:par1>/<int:par2>/mail/', whatsapp, name='whatsapp'),
    path('<str:par1>/<int:par2>/app/', maile, name='mail'),
    path('verify_payment_status/', verify_payment_status, name='verify_payment_status'),
    path('about/', about, name='about')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)