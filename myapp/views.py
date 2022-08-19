from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contact
# Create your views here.
def dashboard(request):
    return render(request,'home.html')
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def hillstations(request):
    return render(request,'hillstations.html')
def lakes(request):
    return render(request,'lakes.html')
def trekking(request):
    return render(request,'trekking.html')
def wildlife(request):
    return render(request,'wildlife.html')
def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        values = Contact(name=name, email=email, desc=desc)
        values.save()
    return render(request,'contact.html')
