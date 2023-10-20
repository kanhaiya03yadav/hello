from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context={
        "variable":"this is sent"
    }
    return render(request,'index.html')
    # return HttpResponse("this is the home-page")
def About(request):
     return render(request,'about.html')
    # return HttpResponse("this is the About")
def games(request):
     return render(request,'games.html')
    
def contact(request):
    if request.method == "POST":
     name= request.POST.get('name')
     email= request.POST.get('email')
     phone= request.POST.get('phone')
     desc= request.POST.get('desc')
     contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
     contact.save()
     messages.success(request,'Your message has been sent!.')

    return render(request,'Contact.html')