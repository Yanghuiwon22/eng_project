from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import ReserveMeal
from itertools import chain
from django.views.generic import CreateView

# Create your views here.
def reserve_main(request):
    all_users = User.objects.exclude(pk=request.user.pk)

    return render(request, 'reserve_meal/reserve_main.html',
                  {'all_users': all_users})

class ReserveMeal_Form(CreateView):
    model = ReserveMeal
    fields = ['receiver','timetable','content']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.sender = current_user
            return super(ReserveMeal_Form, self).form_valid(form)


