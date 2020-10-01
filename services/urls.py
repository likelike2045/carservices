from django.urls import path, include
from services import views
from django.conf import settings
from django.conf.urls.static import static

app_name='services'
urlpatterns = [

    path('', views.home, name='index'),
    path('servicing/<int:id>', views.car_detail, name='car_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)