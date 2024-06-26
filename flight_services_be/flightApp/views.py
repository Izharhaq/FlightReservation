from django.shortcuts import render
from flightApp.models import Flight,Passenger,Reservation
from flightApp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
###########################################
###########################################
# @api_view(['GET','POST'])
# def reservation_operations(request):

#     if request.method =='POST':
#         students = Student.objects.filter(departureCity=departureCity,arrivalCity=arrivalCity,dateOfDeparture=dateOfDeparture)
#         serializer=StudentSerializer(students,many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

###########################################
###########################################

# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights=Flight.objects.filter(departureCity=request.data['departureCity'], arrivalCity=request.data['arrivalCity'], dateOfDeparture=request.data['dateOfDeparture'])
    serializer=FlightSerializer(flights, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def save_reservation(request):
    flight=Flight.objects.get(id=request.data['flightId'])

    passenger=Passenger()
    passenger.firstName=request.data['firstname']
    passenger.lastName=request.data['lastname']
    passenger.middleName=request.data['middlename']
    passenger.email=request.data['email']
    passenger.phone=request.data['phone']
    passenger.save()

    reservation=Reservation()
    reservation.flight=flight
    reservation.passenger= passenger

    Reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['departureCity', 'arrivalCity','dateOfDeparture']



class PassengerViewSet(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer

