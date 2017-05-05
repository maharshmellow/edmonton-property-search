from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

def index(request):
    return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"11620 41 AVENUE SW","garage":"No", "neighbourhood":"ALLARD", "type":"Residential", "latitude":53.39839929, "longitude":-113.5248195, "price":"$8,468,500"})

def redirect(request):
    """This function is run when a user enters a new address into the app"""
    address = request.GET['address']
    conn = sqlite3.connect("properties.db")
    c = conn.cursor()

    c.execute("SELECT address, neighbourhood, garage, type, latitude, longitude, value FROM properties WHERE address like :address;", {"address":address})
    rows = c.fetchall()
    conn.close()

    # Convert garage value from Y, N to Yes, No
    if rows[0][2] == "Y":
        garage = "Yes"
    else:
        garage = "No"

    # Render the page
    if len(rows) == 0:
        # invalid address
        return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"Invalid Address","garage":"", "neighbourhood":"", "type":"", "latitude":"", "longitude":"","price":""})
    else:
        return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":rows[0][0], "neighbourhood":rows[0][1], "garage":garage, "type":rows[0][3], "latitude":rows[0][4], "longitude":rows[0][5],"price":rows[0][6]})
