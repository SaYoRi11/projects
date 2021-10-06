from rest_framework.serializers import ModelSerializer
from .models import Project, TimeEntry

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'due_date']

class TimeEntrySerializer(ModelSerializer):
    class Meta:
        model = TimeEntry
        fields = ['id', 'name', 'startedAt', 'finishedAt', 'duration', 'date', 'projectId']

    