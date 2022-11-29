from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=15)
    members = models.CharField(max_length=140)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    