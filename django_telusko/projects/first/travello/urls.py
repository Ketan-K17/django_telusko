from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('destination/', views.destination, name='destination'),
    path('destination_details/', views.destination_details, name='destination_details'),
    path('elements/', views.elements, name='elements'),
    path('blog/', views.blog, name='blog'),
    path('single_blog/', views.single_blog, name='single_blog'),
    path('contact/', views.contact, name='contact'),
] 