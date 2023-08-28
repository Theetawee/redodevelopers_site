from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Newsletter(models.Model):
    email=models.EmailField()
    timeadded=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email
    
    

class HepB(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    SCHOOLS = [
        ('N', 'School of Nursing'),
        ('A', 'School of Allied Sciences')
    ]
    STATES = [
        ('1', 'Immunized the first time'),
        ('2', 'Immunized second dose'),
        ('3', 'Immunized third dose'),
        ('N', 'Not yet immunized')
    ]
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)
    phone = PhoneNumberField()
    school = models.CharField(choices=SCHOOLS, max_length=1)
    state = models.CharField(choices=STATES, max_length=1)
    added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
