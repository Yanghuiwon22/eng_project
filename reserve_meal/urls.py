from django.contrib import admin
from django.urls import path, include
from .views import reserve_main, ReserveMeal_Form

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', reserve_main, name='reserve_main'),
    path('regi/', ReserveMeal_Form.as_view(), name='reserve_regi')

]
