from django.db import models
import os
from django import forms
# Create your models here.
# 게시글 내용
class BookStore(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='bookstore/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='bookstore/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table = 'blog_post'


    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/bookstore/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

class BookForm_Mod(models.Model):
    # 필드 추가
    책_이름 = models.CharField(max_length=100)
    지은이 = models.IntegerField()
    출판사 = models.CharField(max_length=100)
    필기흔적_opt = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    필기흔적 = models.CharField(max_length=10, choices=필기흔적_opt)

