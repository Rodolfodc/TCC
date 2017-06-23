from django.conf.urls import url

from . import views


app_name = 'test_upload'
urlpatterns = [
url(r'^$', views.model_form_upload, name='upload'),
# ex: /polls/5
# url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
]