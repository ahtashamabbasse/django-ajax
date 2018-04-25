from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^createBook/$', views.createBook, name='createBook')

]
