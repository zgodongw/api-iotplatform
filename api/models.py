from django.db import models

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Site(models.Model):
    place = models.CharField(max_length=256)
    province = models.CharField(max_length=255)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.place

class Asset(models.Model):
    deviceName = models.CharField(max_length=256)
    deviceID = models.CharField(max_length=255, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    location = models.CharField(max_length=256)

    def __str__(self):
        return "{} at {}".format(self.deviceID, self.location)

class Activity(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    temperature = models.DecimalField(max_digits=7, decimal_places=2)
    vibrations = models.DecimalField(max_digits=7, decimal_places=2)
    cashAmount = models.IntegerField()
    cashDeposits = models.IntegerField()
    transactionSpeed = models.DecimalField(max_digits=7, decimal_places=2)
    humidity = models.IntegerField()
    downloadSpeed = models.DecimalField(max_digits=7, decimal_places=2)
    paperLevel = models.IntegerField()
    # Rest of the Attributes will go here

    def __str__(self):
        return "Activity from {}".format(self.asset)