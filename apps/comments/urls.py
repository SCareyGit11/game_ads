from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^add/(?P<id>\d+)$', views.add, name='add'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]