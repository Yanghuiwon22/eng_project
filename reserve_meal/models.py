from django.db import models
from django.contrib.auth.models import User

def reserve_upload_to(instance,filename):
    sender_username = instance.sender.username if instance.sender else 'unknown_sender'
    return f'reserve_meal/images/{instance.sender_username}/{filename}/'

# Create your models here.
class ReserveMeal(models.Model):
    sender = models.ForeignKey(User, related_name='sent_reserve', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_reserve', on_delete=models.CASCADE)

    timetable = models.ImageField(upload_to=reserve_upload_to)


