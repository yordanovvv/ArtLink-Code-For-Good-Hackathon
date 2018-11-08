import json
from urllib.request import urlopen
#from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
#from codeforgood.models import Users, Locations, Tags, Location_Tags, Favourites, Saved_Searches
#from django.contrib.auth import authenticate, login
#from django.core.urlresolvers import reverse
#from django.shortcuts import render
#from social.forms import RegistrationForm, UserProfileForm
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeforgood.settings')
import django
django.setup()
from codeforgood.models import Locations, Tags, Location_Tags, Categories, Favourites
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.http import HttpResponse
import datetime
#from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals
from math import sin, cos, sqrt, atan2, radians
# import re
# approximate radius of earth in km


def getLocation():


    url = 'http://ipinfo.io?token=b4c8c534242400'
    response =urlopen(url)
    data = json.load(response)
    loc = data['loc']
    return loc

def calculateDistance(lat, lon):
    location = getLocation().split(',')
    R = 6373.0
    lat1 = radians(float(location[0]))
    lon1 = radians(float(location[1]))
    lat2 = radians(lat)
    lon2 = radians(lon)
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def index(request):
    return render(request, 'index.html')

def add_location(request):
    return render(request, 'add_location.html')

def list_loc_by_distance(list_loc):
    distances = []
    array1= list_loc[:]
    for location in list_loc:
        distances.append(calculateDistance(location.latitude,location.longitude))
    for x in range(0,len(distances)):
        if(distances[x] > 20):
            distances.pop(x)
            array1.pop(x)
            x -=1
    return array1


def search(request):
    input = request.GET.get('query','')
    return render(request, "search.html", {"locations":search_func(input), "search":request.GET.get("query","")})

def search_func(input):
    good_input = input.split()
    tags = Tags.objects.all()
    tags_location = Location_Tags.objects.all()  #
    tags_list = []
    tags_final = []
    locations = Locations.objects.all()
    results = []
    if not good_input:
        return locations
    if (good_input[0] != ""):
        for input in good_input:
            for tag in tags:
                if (input.lower() == tag.tag.lower()):
                    tags_list.append(tag)
        for tag in tags_list:
            for tag_loc in tags_location:
                if (tag.tag.lower() == tag_loc.tag.tag.lower()):
                    tags_final.append(tag_loc)
        for location in locations:
            islocation = False
            for input in good_input:
                if (location.name.lower().find(input.lower()) != -1):
                    results.append(location)
                    islocation = True
                    break
            if (not islocation):
                valid = False
                for tag in tags_final:
                    if (tag.location == location):
                        results.append(location)
                        valid = True
                        break
                if (not valid):
                    for input in good_input:
                        if (location.description.lower().find(input.lower()) != -1):
                            results.append(location)
                            break;
        list_of_locations = results
        return list_of_locations
    else:
        return locations


def addLocation(request):

    loc_name = request.POST.get('name')
    loc_place = request.POST.get('place')
    loc_description = request.POSTget('description')
    if not(loc_name and loc_place and loc_description):
        return django.http.HttpResponseBadRequest()
    loc_date = request.POST.get('date', "")
    lan = request.POST.get('name',"")
    lon= request.POST.get('name',"")
    contact_name= request.POST.get('name',"")
    contact_num = request.POST.get('name',"")
    contact_email = request.POST.get('name',"")
    website = request.POST.get('website',"")
    cost = request.POST.get('cost',"")
    user = request.POST.get('user', "NULL")
    location = Locations(loc_name,lan,lon,loc_place,contact_name,contact_num,contact_email,website,cost,loc_description,loc_date,user)[0]
    location.save()

def user(request):
	uid = request.GET.get('user_id')
	 # list of ids of locations
	favourites = Favourites.objects.filter(id=uid)
	favs = [Locations(id=i) for i in favourites]
	return render(request, "user.html", {"user":User(id=uid), "favs": favs})

