from django.urls import path, include
from rest_framework.routers import DefaultRouter
from flightApp.views import FlightViewSet, PassengerViewSet, ReservationViewSet, FindFlightsView, SaveReservationView

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    path('findflights/', FindFlightsView.as_view(), name='find-flights'),
    path('savereservation/', SaveReservationView.as_view(), name='save-reservation'),
    path('', include(router.urls)),
]
