from django.urls import path, include
from . import  views

urlpatterns = [

    # path('<int:pk>/', views.BookStoreDetail.as_view()),
    path('', views.BookStoreList.as_view()),
    # path('register/', views.BookStoreRegister.as_view(), name='book_register'),
    path('custom/', views.my_custom_view, name='custom_form'),
]