from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Data

class DataList(ListView):
    model = Data
    ordering = '-pk'

class DataDetail(DetailView):
    model = Data