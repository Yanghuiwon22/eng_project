from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Data

# Create your views here.
class DataList(ListView):
    model = Data
    ordering = '-pk'

class DataDetail(DetailView):
    model = Data