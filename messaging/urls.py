from django.urls import path
from .views import new_message

urlpatterns = [
    # 기존 URL 패턴들...
    path('new_messaing', new_message, name='new_message'),
    # 기타 패턴들...
]