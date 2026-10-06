from django.db import models

class VehicleService_DB(models.Model):
    Service_ID = models.IntegerField()
    Customer_Name = models.CharField(max_length=30)
    Vehicle_No = models.CharField(max_length=15)
    Vehicle_Type = models.CharField(max_length=20)
    Service_Type = models.CharField(max_length=30)
    Service_Date = models.DateField()
    Amount = models.FloatField()
    Status = models.CharField(max_length=20)
