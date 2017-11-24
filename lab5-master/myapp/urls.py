from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^order/(?P<id>(\d+))$', views.orders, name='order_url'),
    url(r'^$', views.index,  name='index')
]