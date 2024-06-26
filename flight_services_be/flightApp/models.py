from django.db import models

# Create your models here.

class Flight(models.Model):
    flightNumber=models.CharField(max_length=10)
    operatingAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20)
    arrivalCity=models.CharField(max_length=20)
    dateOfDeparture=models.DateField()
    estimatedTimeOfDeparture=models.TimeField()

class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

class Reservation(models.Model):
    # flight = models.OneToOneField(Flight,on_delete=models.CASCADE)    # one to one relationship
    flight = models.ForeignKey(Flight,on_delete=models.CASCADE) # many to onen relationship
    passenger = models.OneToOneField(Passenger,on_delete=models.CASCADE)