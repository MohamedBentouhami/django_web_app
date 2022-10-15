from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing

def band_list(request):
    bands = Band.objects.all()
    return render(request,'groups/band_list.html',{'bands':bands})

def band_detail(request,id):
    band = Band.objects.get(id=id)
    return render(request,'groups/band_detail.html',{'band':band})

def about(request):
    return render(request,'about.html')

def listing(request):
    listings = Listing.objects.all()
    return render(request,'listings/listing.html',{'listings':listings})
def listing_detail(request,id):
    listing = Listing.objects.get(id=id)
    return render(request,'listings/listing_detail.html',{'listing':listing})

def contact(request):
    return render(request,'contact.html')