from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Notice

class NoticeList(ListView):
    model = Notice
    ordering = '-pk'

class NoticeDetail(DetailView):
    model = Notice