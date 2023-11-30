from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import BookStore
from django.urls import reverse_lazy
from .models import BookStore, Category
from django.contrib.auth.mixins import LoginRequiredMixin

class BookStoreList(ListView):
    model = BookStore
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(BookStoreList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = BookStore.objects.filter(category=None).count()

        return context

class BookStoreDetail(DetailView):
    model = BookStore
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super(BookStoreDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = BookStore.objects.filter(category=None).count()

        return context

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
        'bookstore/templates/bookstore/bookstore_form.html',
        {
            'form': form,
        }
    )

class BookForm_Form(CreateView):
    model = BookStore
    fields = ['title', 'author', 'publisher', 'category','price', 'img_file', 'content', 'traces', 'status']  # 필요한 필드들을 지정
