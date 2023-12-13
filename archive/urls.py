# from django.urls import path, include
# from . import  views
#
# urlpatterns = [
#     # path('<int:pk>/',views.single_post_page),
#     # path('', views.index),
#     path('<int:pk>/', views.DataDetail.as_view()),
#     path('', views.DataList.as_view()),
#
# ]


from django.urls import path
from .views import ArchiveList, ArchiveDetail, ArchiveForm_Form, archiveform_view, category_page

app_name = 'archive'

urlpatterns = [
    path('<int:pk>/', ArchiveDetail.as_view(), name='archive_detail'),
    path('archive_list/', ArchiveList.as_view(), name='archive_list'),
    path('archive_form/', ArchiveForm_Form.as_view(), name='archive_form'),
    path('archiveform_view/', archiveform_view, name='archiveform_view'),
    path('category/<slug:slug>/', category_page, name='category_page'),
]
