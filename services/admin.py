from django.contrib import admin
from .models import Services, Car
# Register your models here.


class CarAdmin(admin.ModelAdmin):
    list_display = ('car_model', 'car_owner', 'car_notes',
    	'car_number', 'description', 'services_type',
    	'submission_date', 'year_old', 'services_charge',
    	)

admin.site.register(Services)
admin.site.register(Car, CarAdmin)