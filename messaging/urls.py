from django.urls import path
from . import  views
from reserve_meal.views import reserve_list

urlpatterns = [
    # 기존 URL 패턴들...
    path('new_messaing/', views.create_message, name='new_message'),
    path('message_list/', views.message_list, name='message_list'),
    path('reserve_list/', reserve_list, name='reserve_list'),

    # path('<int:user.id>/', views.message_list, name='message_details'),

]