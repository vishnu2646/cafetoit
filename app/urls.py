from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('menu/',views.menu,name="menu"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('service/',views.service,name="service"),
    path('gallery/',views.GalleryListView.as_view(),name="gallery"),
    path('blog/',views.PostListView.as_view(),name="blog"),
    path('detail/<int:pk>/',views.PostDetailView.as_view(),name="detail"),
]
