

from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('themes', themes, name='themes'),
    path('blog-details-1', blogdetails1, name='blogdetails1'),
    path('blog-details-2', blogdetails2, name='blogdetails2'),
    path('blog-details-3', blogdetails3, name='blogdetails3'),
    path('blog-details-4', blogdetails4, name='blogdetails4'),
]
