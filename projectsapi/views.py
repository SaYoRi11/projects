from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectSerializer, TimeEntrySerializer
from .models import Project, TimeEntry

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TimeEntryViewSet(ModelViewSet):
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
