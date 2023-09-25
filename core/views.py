from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def themes(request):
    return render(request, 'themes.html')

# blogs

def blogs(request):
    return render(request, 'blog.html')
def blogdetails1(request):
    return render(request, 'blog-details1.html')
def blogdetails2(request):
    return render(request, 'blog-details2.html')
def blogdetails3(request):
    return render(request, 'blog-details3.html')
def blogdetails4(request):
    return render(request, 'blog-details4.html')

def works(request):
    return render(request, 'works.html')

def contact(request):
    return render(request, 'contact.html')

def terms(request):
    return render(request, 'terms.html')

def policy(request):
    return render(request, 'policy.html')