from django.shortcuts import render
from django.http import Http404
from .models import Car

# Create your views here.
def home(request):
	cars = Car.objects.all()
	context = {'cars':cars}

	return render(request, 'services/home.html', context)


def car_detail(request, id):
	try:
		car = Car.objects.get(id=id)
	except Car.DoesNotExist:
		raise Http404('Car not found')
	
	return render(request, 'services/car_detail.html', {'car':car})