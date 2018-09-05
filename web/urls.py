from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^date', views.getdatetime, name='getDate'),
    url(r'^websocket', views.websocket, name='webSocket'),
]
