from django.urls import path, include
from . import  views

urlpatterns = [
    path('<int:pk>/', views.BookStoreDetail.as_view()),
    path('', views.BookStoreList.as_view(), name='bookstore_list'),
    path('register/', views.BookForm_Form.as_view(), name='bookstore_register_form'),
    # path('list/', views.booklist_view(), name='booksotre'),
]