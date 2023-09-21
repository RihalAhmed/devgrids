from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def themes(request):
    return render(request, 'themes.html')

def contact(request):
    return render(request, 'contact.html')