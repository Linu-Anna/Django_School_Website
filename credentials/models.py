from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=5000, null=True, blank=True)

