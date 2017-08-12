from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
import json

def index(request):
    return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"11620 41 AVENUE SW","garage":"NO", "neighbourhood":"ALLARD", "type":"RESIDENTIAL", "latitude":53.39839929, "longitude":-113.5248195, "price":"$8,468,500"})

def redirect(request):
    """This function is run when a user enters a new address into the app"""
    try:
        address = request.GET['address']
    except:
        return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"INVALID ADDRESS","garage":"", "neighbourhood":"", "type":"", "latitude":"", "longitude":"","price":""})

    if len(address) == 0:   # need to check this since the database contains some empty address lines
        return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"INVALID ADDRESS","garage":"", "neighbourhood":"", "type":"", "latitude":"", "longitude":"","price":""})

    conn = sqlite3.connect("properties.db")
    c = conn.cursor()
    c.execute("SELECT address, neighbourhood, garage, type, latitude, longitude, value FROM properties WHERE address like :address;", {"address":address})
    rows = c.fetchall()
    conn.close()

    # Render the page
    if len(rows) == 0:
        # invalid address
        return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":"INVALID ADDRESS","garage":"", "neighbourhood":"", "type":"", "latitude":"", "longitude":"","price":""})
    else:
        # Convert garage value from Y, N to Yes, No
        if rows[0][2] == "Y":
            garage = "Yes"
        else:
            garage = "No"

        return render(request, "pricer/header.html", {"addressBarValue":"Enter Address", "address":rows[0][0], "neighbourhood":rows[0][1], "garage":garage.upper(), "type":rows[0][3].upper(), "latitude":rows[0][4], "longitude":rows[0][5],"price":rows[0][6]})

def addresses(request):
    """This function is used for the autocomplete"""
    query = request.GET['query']

    responseAddresses = []

    # returns the 20 addresses that contain the query typed in
    conn = sqlite3.connect("properties.db")
    c = conn.cursor()
    
    # see if we can get 7 items that start with the input value - if there are less, we can check to see if the the input value exists inbetween strings in the database
    c.execute("SELECT address FROM properties WHERE address like :address limit 7;", {"address":query+"%"})
    
    rows = c.fetchall()
    remaining = 7 - len(rows)

    if remaining > 0:
        c.execute("SELECT address FROM properties WHERE address like :address limit :remaining;", {"address":"%"+query+"%", "remaining": remaining})
        
        for new_item in c.fetchall():
            if new_item not in rows:
                rows.append(new_item)

    conn.close()

    for row in rows:
        responseAddresses.append(row[0])
        print(row)

    return HttpResponse(json.dumps({"suggestions":responseAddresses}))
