from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to ALX Travel App Listings!"})
