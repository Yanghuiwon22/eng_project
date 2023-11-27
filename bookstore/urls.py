from django.urls import path, include
from . import  views

urlpatterns = [

    # path('<int:pk>/', views.BookStoreDetail.as_view()),
    path('', views.BookStoreList.as_view()),
    # path('register/', views.BookStoreRegister.as_view(), name='book_register'),
    path('custom/', views.bookform_view, name='bookstore_register_form'),
]