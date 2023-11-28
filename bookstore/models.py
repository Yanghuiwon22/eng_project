from django.db import models
import os
from PIL import Image

from django import forms
# Create your models here.
# 게시글 내용
class BookStore(models.Model):
    title = models.CharField(max_length=100)
    지은이 = models.CharField(max_length=100)
    출판사 = models.CharField(max_length=100)
    필기흔적_opt = [
        ('밑줄(연필/샤프)', '밑줄(연필/샤프)'),
        ('밑줄(볼펜/형광펜)', '밑줄(볼펜/형광펜)'),
        ('필기(연필/샤프)', '필기(연필/샤프)'),
        ('필기(볼펜/형광펜)', '필기(볼펜/형광펜)'),
    ]
    필기흔적 = models.CharField(max_length=10, choices=필기흔적_opt)
    보존상태_opt = [
        ('밑줄(연필/샤프)', '겉표지 깨끗함'),
        ('밑줄(볼펜/형광펜)', '이름(서명) 기입 없음'),
        ('필기(연필/샤프)', '페이지 변색 없음'),
        ('필기(볼펜/형광펜)', '페이지 훼손'),
    ]
    보존상태 = models.CharField(max_length=10, choices=보존상태_opt)
    img_file = models.ImageField(upload_to='bookstore/images/%Y/%m/%d', blank=True)
    희망가격 = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.출판사}] {self.title}'

    def get_absolute_url(self):
        return f'/bookstore/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.img_file.name)

    def get_file_ext(self):
        return self.img_file().split('.')[-1]

# class BookForm_Mod(models.Model):
#     # 필드 추가
#     책_이름 = models.CharField(max_length=100)
#     지은이 = models.CharField(max_length=100)
#     출판사 = models.CharField(max_length=100)
#     필기흔적_opt = [
#         ('밑줄(연필/샤프)', '밑줄(연필/샤프)'),
#         ('밑줄(볼펜/형광펜)', '밑줄(볼펜/형광펜)'),
#         ('필기(연필/샤프)', '필기(연필/샤프)'),
#         ('필기(볼펜/형광펜)', '필기(볼펜/형광펜)'),
#     ]
#     필기흔적 = models.CharField(max_length=10, choices=필기흔적_opt)
#     보존상태_opt = [
#         ('밑줄(연필/샤프)', '겉표지 깨끗함'),
#         ('밑줄(볼펜/형광펜)', '이름(서명) 기입 없음'),
#         ('필기(연필/샤프)', '페이지 변색 없음'),
#         ('필기(볼펜/형광펜)', '페이지 훼손'),
#     ]
#     보존상태 = models.CharField(max_length=10, choices=보존상태_opt)
#     img_file = models.FileField(upload_to='bookstore/images/%Y/%m/%d', blank=True)
#     희망가격 = models.CharField(max_length=100)
#


