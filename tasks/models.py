from django.db import models

class TaskStatus(models.Model):
    description = models.CharField(max_length=50)
    color = models.CharField(max_length=10)


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.ForeignKey(TaskStatus, models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
