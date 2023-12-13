from django.urls import path, include
from . import  views

urlpatterns = [
    path('<int:pk>/', views.ArchiveDetail.as_view()),
    path('', views.ArchiveList.as_view(), name='archive_list'),
    path('register/', views.ArchiveForm_Form.as_view(), name='archive_register_form'),
    path('archive/category/<str:slug>', views.category_page)
]

