from django.db import models

# Create your models here.



class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Course(models.Model):
    department= models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name





