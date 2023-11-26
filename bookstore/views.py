from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import BookStore
from .form import UserForm

class BookStoreList(ListView):
    model = BookStore
    ordering = '-pk'


class BookStoreDetail(DetailView):
    model = BookStore

def user_input(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            return redirect('success_url_name')
            # 여기에서 필요한 로직을 수행하거나 데이터베이스에 저장할 수 있습니다.
            # 예: User.objects.create(name=name, email=email)
            U
            return render(request, 'success_template.html', {'name': name, 'email': email})
    else:
        form = UserForm()
    return render(request, 'bookstore/bookstore_list.html', {'form': form})

def to_book_reg(request):
    return render(request, 'bookstore/.html')