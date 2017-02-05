from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^users$', views.create, name='create'),
    url(r'^login$', views.show, name='show')
]