from django.http import HttpResponse
from django.shortcuts import render

# # Create your views here.
def index(request):
    return render(request, "pricer/header.html", {"addressBarField":"Enter Address", "address":"1708 62 Street SW","garage":"Yes", "type":"Residential", "longitude":54.32993, "latitude":-112.3232, "price":"$1,000,000"})
    #return HttpResponse("Testing")
