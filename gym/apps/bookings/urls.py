from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet

router = DefaultRouter()
router.register('bookings', BookingViewSet, basename='trainer')

urlpatterns = [
    path('', include(router.urls)),
]
