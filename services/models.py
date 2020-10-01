from django.db import models

# Create your models here.
# max_length variable
max_len = 100
min_len = 1
length_thirty = 30
length_fifty = 50

class Services(models.Model):
	name = models.CharField(max_length=length_fifty)

class Car(models.Model):
	SERVICE_CHOICES = [('P','Platinum'),('G','Gold')]
	car_model = models.CharField(max_length=max_len)
	car_owner = models.CharField(max_length=max_len)
	car_notes = models.CharField(max_length=max_len)
	car_number = models.CharField(max_length=length_thirty)
	description = models.TextField()
	services_type = models.IntegerField(choices = SERVICE_CHOICES, max_length=min_len, blank=True)
	submission_date = models.DateTimeField()
	year_old = models.IntegerField()
	services_charge = models.IntegerField(null=True)
	servicing = models.ManyToManyField(Services, blank=True)


	
	