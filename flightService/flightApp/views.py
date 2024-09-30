from django.shortcuts import render
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlighSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['POST'])
def find_flight(request):
    flights = Flight.objects.filter(departureCity = request.data['departureCity'], arrivalCity = request.data['arrivalCity'])
    serializer = FlighSerializer(flights, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    print(request.data)
    flight = Flight.objects.get(id = request.data['flightId'])
    passenger = Passenger()
    passenger.firstName = request.data['firstName']
    passenger.lastName = request.data['lastName']
    passenger.middleName = request.data['middleName']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save(passenger)

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger
    Reservation.save(reservation)

    return Response(status = status.HTTP_201_CREATED)




class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlighSerializer
    permission_classes = (IsAuthenticated)


class PassengertViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = (IsAuthenticated)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated)
