from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    due_date = models.DateField()

class TimeEntry(models.Model):
    name = models.CharField(max_length=50)
    startedAt = models.TimeField()
    finishedAt = models.TimeField()
    duration = models.TimeField()
    date = models.DateField()
    projectId = models.ForeignKey(Project, on_delete = models.CASCADE, related_name='time_entries')



