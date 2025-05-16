from django.db import models

# Create your models here.
class Patient(models.Model):
    hospital_id = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
