from django.shortcuts import render
from .models import Post,Gallery
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
# Create your views here.
def index(request):
    return render(request,'home.html')

def menu(request):
    return render(request,'menu.html')

def contact(request):
    return render(request,'contacts.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def gallery(request):
    return render(request,'gallery.html')

class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery.html'
    context_object_name = 'gallerys'

class PostListView(ListView):
    model = Post
    template_name = 'blog.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'details.html'