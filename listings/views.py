from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "ALX Travel App Listings!"})