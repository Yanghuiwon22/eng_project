from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import BookStore
from django.urls import reverse_lazy
from .form import MyCustomForm

class BookStoreList(ListView):
    model = BookStore
    ordering = '-pk'


class BookStoreDetail(DetailView):
    model = BookStore

# bookregister
def my_custom_view(request):
    if request.method == 'POST':
        form = MyCustomForm(request.POST)
        if form.is_valid():
            # 폼이 유효한 경우, 데이터 처리 로직 작성
            form.save()  # 모델에 저장하거나 추가적인 로직 수행
            return redirect('bookstore_list.html')  # 성공 페이지로 이동
    else:
        form = MyCustomForm()

    return render(request, 'bookstore/bookstore_register.html', {'form': form})


def to_book_reg(request):
    return render(request, 'bookstore/bookstore_detail.html')


