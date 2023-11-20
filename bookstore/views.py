from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BookStore

class BookStoreList(ListView):
    model = BookStore
    ordering = '-pk'

class BookStoreDetail(DetailView):
    model = BookStore