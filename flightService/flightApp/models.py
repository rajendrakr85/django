from django.db import models


class Flight(models.Model):
    flightNumber = models.CharField(max_length=10)
    operatingAirLines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return self.flightNumber +" from: "+self.departureCity+" arrival:"+self.arrivalCity +" on: "+self.dateOfDeparture


class Passenger(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName +" "+self.middleName+" "+self.lastName

class Reservation(models.Model):
     passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
     flight = models.OneToOneField(Flight, on_delete=models.CASCADE)