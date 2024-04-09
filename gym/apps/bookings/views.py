from rest_framework import viewsets

from gym.apps.bookings.models import Booking
from gym.apps.bookings.serializers import BookingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
