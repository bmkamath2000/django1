from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    gender=models.CharField(max_length=6)
    dob = models.DateField()
    def __str__(self):
        return self.first_name + ' '+ self.last_name