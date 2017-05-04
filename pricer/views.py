from django.http import HttpResponse
from django.shortcuts import render

# # Create your views here.
def index(request):
    return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"11620 41 AVENUE SW","garage":"No", "neighbourhood":"ALLARD", "type":"Residential", "latitude":53.39839929, "longitude":-113.5248195, "price":"$8,468,500"})
    #return HttpResponse("Testing")


def redirect(request):
    address = request.GET['address']
    return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":address,"garage":"No", "neighbourhood":"ALLARD", "type":"Residential", "latitude":53.39839929, "longitude":-113.5248195, "price":"$8,468,500"})
