from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=70)
    lname = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=90)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()
    
    def __str__(self):
        return f"{self.fname} {self.lname}"
