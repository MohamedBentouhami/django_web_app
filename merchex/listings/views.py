from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band

def hello(request):
    bands = Band.object.all()
    return HttpResponse('<h1>Hello Django ! </h1>')

def about(request):
    return HttpResponse('<h1>About</h1><p>We love merch !</p>')

def listing(request):
    return HttpResponse('listings')

def contact(request):
    return HttpResponse('contact')