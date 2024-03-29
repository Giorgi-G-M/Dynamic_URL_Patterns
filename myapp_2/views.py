from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def name(request,names):
    return HttpResponse(f"<h1>Hello {names}</h1>")