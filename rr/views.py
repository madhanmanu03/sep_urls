from django.shortcuts import render
from django.http import HttpResponse

def sanju(request):
    return render(request,'sanju.html')