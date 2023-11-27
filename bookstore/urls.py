from django.urls import path, include
from . import  views

urlpatterns = [

    # path('<int:pk>/', views.BookStoreDetail.as_view()),
    path('', views.BookStoreList.as_view()),
    path('bookstore_datail/', views.BookStoreDetail.as_view(), name='to_book_reg'),

]