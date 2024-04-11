
from django.contrib import admin
from django.urls import path
from first import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage , name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('submitform/', views.submitform, name='submitform'),
    path('marksheet/', views.marksheet, name='marksheet'),
    path('detailview/<slug>', views.detailview),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)