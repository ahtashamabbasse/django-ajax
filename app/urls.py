from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createBook/$', views.createBook, name='createBook'),
    url(r'^book/(?P<id>\d+)/update/$', views.updateBook, name='updateBook'),
    url(r'^book/(?P<id>\d+)/delete/$', views.deleteBook, name='deleteBook'),

]
