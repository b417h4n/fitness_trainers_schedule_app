from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ScheduleViewSet

router = DefaultRouter()
router.register('schedules', ScheduleViewSet, basename='trainer')

urlpatterns = [
    path('', include(router.urls)),
]
