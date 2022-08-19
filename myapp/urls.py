from django.urls import path
from . import views
urlpatterns= [
    path('',views.dashboard, name='Dashboard'),
    path('home/',views.home, name='Home'),
    path('about/',views.about, name='About'),
    path('hillstations/',views.hillstations, name='Hillstations'),
    path('lakes/',views.lakes, name='Lakes'),
    path('trekking/',views.trekking, name='Trekking'),
    path('wildlife/',views.wildlife, name='Wildlife'),
    path('contact',views.contact, name='Contact'),

]