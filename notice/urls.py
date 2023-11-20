from django.urls import path, include
from . import  views

urlpatterns = [

    path('<int:pk>/', views.NoticeDetail.as_view()),
    path('', views.NoticeList.as_view())

]