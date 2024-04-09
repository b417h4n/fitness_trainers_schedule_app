from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import GymViewSet

router = DefaultRouter()
router.register('gyms', GymViewSet, basename='trainer')

urlpatterns = [
    path('', include(router.urls)),
]
