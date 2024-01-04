from django.db import models

# Create your models here.

class musician(models.Model):

    Choice_instrument=[
        ('guitar','Guitar'),
        ('tabla','Tabla'),
        ('harmnony','Harmnony'),
        ('behala','Behala'),
        ('ektara','Eektara'),
        
    ]

    FirstName=models.CharField(max_length=100,unique=True)
    LastName=models.CharField(max_length=100,unique=True)
    Email=models.EmailField(max_length=100)
    PhoneNumber=models.CharField(max_length=15)
    InstrumentType=models.CharField(max_length=100,choices=Choice_instrument)

    def __str__(self) -> str:
        return self.FirstName + ' ' + self.LastName 
