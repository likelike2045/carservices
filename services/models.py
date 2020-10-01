from django.db import models

# Create your models here.
# max_length variable
max_len = 100


class Car(models.Model):
	SERVICE_CHOICES = [()]
	car_model = models.CharField(max_length=max_len)
	car_owner = models.CharField(max_length=max_len)
	car_notes = models.CharField(max_length=max_len)
	car_number = models.CharField(max_length=30)
	description = models.TextField()
	services_type = models.IntegerField(choices = )
	services_charge = models.IntegerField()



	name = models.CharField(max_length=max_len)
	
	