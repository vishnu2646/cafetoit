from django.shortcuts import render

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