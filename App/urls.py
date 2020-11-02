from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from App import views
from django.views.static import serve
from django.conf.urls import url
urlpatterns = [
    path('', views.skin, name='intro'),
    path('upload2',views.upload2,name='intro'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)