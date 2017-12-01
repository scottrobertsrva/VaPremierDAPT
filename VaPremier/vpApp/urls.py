from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^fiscal/(?P<fy>[A-Za-z0-9]+)$',views.fy, name='fy2016'),
    url(r'^getJson',views.objectApi,name='index'),
    
]
