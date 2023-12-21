from django.urls import path
from .views import create_message, message_list
from reserve_meal.views import reserve_list

urlpatterns = [
    # 기존 URL 패턴들...
    path('new_messaing/', create_message, name='new_message'),
    path('message_list/', message_list, name='message_list'),
    path('reserve_list/', reserve_list, name='reserve_list'),
    # path('reserve_list/<int:pk>', name='reserve_message_detail')
]