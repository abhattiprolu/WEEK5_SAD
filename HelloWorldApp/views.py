from django.shortcuts import render

# Create your views here.

# HelloWorldApp/views.py
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"Message": "Hello World!"})

