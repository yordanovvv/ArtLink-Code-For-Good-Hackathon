from django.db import models
from django.contrib.auth.models import User


# class Users(models.Model):
#     username = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     # address = models.CharField(max_length=255)
#     # phone = models.CharField(max_length=255)
#     # dob = models.DateTimeField()


class Locations(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_num = models.CharField(max_length=255)
    contact_email = models.CharField(max_length=255)
    website = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    description = models.CharField(max_length=4095)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, default=None)

    def __str__(self):
        return self.name


class Tags(models.Model):
    tag = models.CharField(max_length=255)
    accessibility = models.BooleanField(default = False)


class Location_Tags(models.Model):
    location = models.ForeignKey(Locations, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)


class Favourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    favourite_loc = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True, default=None)


class Saved_Searches(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    location = models.CharField(max_length=255)
    search = models.CharField(max_length=255)


search_filters = models.CharField(max_length=255)


class Suggestions(models.Model):
    loc = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True, default=None)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, default=None)
    suggestion = models.CharField(max_length=6000)


class Warnings(models.Model):
    loc = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True, default=None)
    warning = models.CharField(max_length=255)


class Categories(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)

