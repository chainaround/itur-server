from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcome_home(request):
    #return HttpResponse('Hello World')
    return render(request, 'attenuation/home.html')