from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('menu/',views.menu,name="menu"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
]
