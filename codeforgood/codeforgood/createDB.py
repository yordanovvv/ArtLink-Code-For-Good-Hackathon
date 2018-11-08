from django.db import models

class Users(models.model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    dob = models.DateTimeField()

class Locations(models.model):
    name = models.CharField(max_length=255)
    coords = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    tags = models.CharField(max_length=4095)
    accessbility = models.CharField(max_length=4095)
    date = models.DateField()
    user_id = models.ForeignKey(Users)

    def __str__(self):
        return self.name

class Favourites(models.model):
    user_id = models.ForeignKey(Users)
    favourite_loc_id = models.ForeignKey(Locations)

class Saved_Searches(models.model):
    user_id = models.ForeignKey(Users)
    location = models.CharField(max_length=255)
    search = models.CharField(max_length=255)
search_filters = models.CharField(max_length=255)

class Suggestions(models.model):
    loc_id = models.ForeignKey(Locations)
    user_id = models.ForeignKey(Users)
    suggestion = models.CharField(max_length=6000)

class Warnings(models.model):
    loc_id = models.ForeignKey(Locations)
    warning = models.CharField(max_length=255)

class Categories(models.model):
    category = models.Charfield(max_length=255)
    subcategory = models.CharField(255)




