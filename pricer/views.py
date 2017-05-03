from django.http import HttpResponse
from django.shortcuts import render

# # Create your views here.
def index(request):
    return render(request, "pricer/home.html", {"price":1000, "address":100000, "type":"Residential", "longitude":54.32993, "latitude":-112.3232})
    #return HttpResponse("Testing")
