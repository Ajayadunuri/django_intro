from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse("This is about the view")

def contact(request):
    return HttpResponse("This is the contact view")

def login(request):
    return render(request,"login.html")