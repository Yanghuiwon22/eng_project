from django.urls import path
from . import  views

urlpatterns = [
    # 기존 URL 패턴들...
    path('new_messaing/', views.create_message, name='new_message'),
    path('message_list/', views.message_list, name='message_list')
    # 기타 패턴들...
]