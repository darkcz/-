from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^loginVerify/$', views.loginVerify, name='loginVerify'),
    url(r'^index/$', views.index, name='index'),
]
