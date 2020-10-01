from django.urls import path, include
from services import views

app_name='services'
urlpatterns = [

    path('', views.home, name='index'),
    path('servicing/<int:id>', views.car_detail, name='car_detail'),
]