from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.forms import ContactUsForm
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

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
            subject= f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message = form.cleaned_data['message'],
            from_email = form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],)
        return redirect('email-send')
    
    else:
        form = ContactUsForm()
    
    return render(request,'contact.html',{'form':form})

def email_send(request):
    return render(request,'email_sent.html')