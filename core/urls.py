

from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('contact', contact, name='contact'),
    path('themes', themes, name='themes'),
]
