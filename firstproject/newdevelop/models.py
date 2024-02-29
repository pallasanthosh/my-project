from django.db import models

# Create your models here.
from django.db import models
import uuid


# Create your models here.
class Feature(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    username=models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    country = models.CharField(max_length=50, )
    password1 = models.CharField(max_length=40)

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    employeeid = models.CharField(max_length=30)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    current_salary = models.CharField(max_length=30)
    expected_salary = models.CharField(max_length=30)
    current_domain = models.CharField(max_length=100)
    change_domain = models.CharField(max_length=100)
    skills= models.CharField(max_length=500)
    def __str__(self):
        return self.firstname
    
    
     

