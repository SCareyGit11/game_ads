from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^vote/(?P<id>\d+)$', views.vote, name='vote'),
    url(r'^adpost/(?P<id>\d+)$', views.adpost, name='adpost'),
    # url(r'^add/(?P<id>\d+)$', views.add, name='add'),
    # url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]