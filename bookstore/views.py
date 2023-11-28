from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import BookStore
from django.urls import reverse_lazy
from .form import BookForm_Form

class BookStoreList(ListView):
    model = BookStore
    ordering = '-pk'


class BookStoreDetail(DetailView):
    model = BookStore

# bookregister
def bookform_view(request):     # 폼을 통해 데이터를 입력받고 이를 데이터베이스에 저장
    if request.method == 'POST':
        form = BookForm_Form(request.POST, request.FILES)  # request.FILES로 폼에 입력한 사진을 데이터베이스에 저장할 수 있다.
        if form.is_valid():
            # 폼이 유효한 경우, 데이터 처리 로직 작성
            form.save()  # 모델에 저장하거나 추가적인 로직 수행
            return redirect('bookstore_list')  # 성공 페이지로 이동
    else:
        form = BookForm_Form()

    return render(
        request,
        'bookstore/bookstore_register.html',
        {
            'form': form,
        }
    )

def booklist_view(request):    #데이터베이스에서 모든 포스트를 가져와서 리스트형식으로 보이게 함.
    book = BookStore.objects.all().order_by('-pk')

    return render(
        request,
        'bookstore/bookstore_list.html',
        {'posts': book}
    )


