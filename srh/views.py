from django.shortcuts import render
from django.http import HttpResponse

def kane(request):
    return render(request,'kane.html')