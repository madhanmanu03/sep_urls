from django.shortcuts import render
from django.http import HttpResponse

def msd(request):
    return render(request,'msd.html')