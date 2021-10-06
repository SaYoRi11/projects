from django.urls import path, include
from .views import ProjectViewSet, TimeEntryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('project', ProjectViewSet, basename='project')
router.register('timeentry', TimeEntryViewSet, basename='timeentry')

urlpatterns = [
    path('', include(router.urls))
]