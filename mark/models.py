from django.db import models

class Mark_Class(models.Model):
    Roll_No=models.IntegerField()
    Name=models.CharField(max_length=50)
    Mark_Math=models.IntegerField()
    Mark_physics = models.IntegerField()
    Mark_chemistry = models.IntegerField()
