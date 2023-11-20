from django.urls import path, include
from . import  views

urlpatterns = [
    # path('<int:pk>/',views.single_post_page),
    # path('', views.index),
    path('<int:pk>/', views.DataDetail.as_view()),
    path('', views.DataList.as_view()),

]