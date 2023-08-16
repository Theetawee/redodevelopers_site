from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email=models.EmailField()
    timeadded=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email