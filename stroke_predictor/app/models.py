from django.db import models

# Create your models here.

class Patient(models.Model):
    gender = models.CharField(max_length=8)
    age = models.IntegerField()
    hypertension = models.IntegerField()
    heart_disease = models.IntegerField()
    ever_married = models.CharField(max_length=32)
    work_type = models.CharField(max_length=32)
    residence_type = models.CharField(max_length=32)
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.CharField(max_length=32)
    stroke = models.IntegerField()

    