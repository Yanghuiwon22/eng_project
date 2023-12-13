from django.db import models
from django.contrib.auth.models import User
import uuid


def reserve_upload_to(instance,filename):
    instance.sender_username = instance.sender.username
    extension = filename.split('.')[-1]  # 파일 확장자 추출
    new_filename = f'{uuid.uuid4().hex}.{extension}'

    # return f'reserve_meal/images/%Y/%M/%D/'
    return f'reserve_meal/images/{instance.sender_username}/{new_filename}'

# Create your models here.
class ReserveMeal(models.Model):
    sender = models.ForeignKey(User, related_name='sent_reserve', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_reserve', on_delete=models.CASCADE)

    timetable = models.ImageField(upload_to=reserve_upload_to)
    def get_absolute_url(self):        # 폼을 성공적으로 처리 시 이동할 페이지 주소
        return f'/reserve_meal/'


