from django.db import models

# Create your models here.
# max_length variable


class Services(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __str__(self):
		return self.name

class Car(models.Model):
	PLATINUM = 'PL'
	GOLD = 'GO'
	SERVICE_CHOICES = (
						('PLATINUM','Platinum'),
						('GOLD','Gold'),
					)
	car_model = models.CharField(max_length=100)
	car_owner = models.CharField(max_length=100)
	car_notes = models.CharField(max_length=100)
	car_number = models.CharField(max_length=30)
	description = models.TextField()
	services_type = models.CharField(
									choices = SERVICE_CHOICES, 
									max_length=100, 
									blank=True,
									)
	submission_date = models.DateTimeField()
	year_old = models.IntegerField()
	services_charge = models.IntegerField(null=True, blank=True)
	servicing = models.ManyToManyField(Services, blank=True)


	def __str__(self):
		return f'{self.car_model} - {self.car_notes} - {self.car_number}' 


	
	