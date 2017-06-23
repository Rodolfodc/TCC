from django.conf.urls import url

from . import views

app_name = 'submit'
urlpatterns = [
    url(r'^$', views.upload, name='upload'),
    url(r'^file_upload/$', views.home, name='file_upload'),
    url(r'^simple_upload/$', views.simple_upload, name='simple_upload'),
    url(r'^model_form_upload/$', views.model_form_upload, name='model_form_upload'),
]