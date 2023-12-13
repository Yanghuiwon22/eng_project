from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import BookStore, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import forms


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

class BookForm_Form(LoginRequiredMixin, CreateView):
    model = BookStore
    fields = ['title', 'author', 'publisher', 'writer', 'category', 'price_set', 'price', 'img_file', 'content', 'traces', 'status']
    # success_url = reverse_lazy('bookstore_list')  # 'bookstore_list'는 실제로 리다이렉트할 URL 이름으로 수정해야 합니다.

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.writer = current_user
            return super(BookForm_Form, self).form_valid(form)
        else:
            return redirect('/bookstore/bookstore_list')


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    book_list = BookStore.objects.filter(category=category)

    return render(
        request,
        'bookstore/bookstore_list.html',
        {
            'book_list' : book_list,
            'categories' : Category.objects.all(),
            'no_category_post_count':BookStore.objects.filter(category=None).count(),
            'category':category,
        }
    )




# from django.shortcuts import render, redirect
# from django.views.generic import ListView, DetailView, CreateView
# from .models import BookStore
# from django.urls import reverse_lazy
# from .models import BookStore, Category
# from django.contrib.auth.mixins import LoginRequiredMixin
#
# class BookStoreList(ListView):
#     model = BookStore
#     ordering = '-pk'
#
#     def get_context_data(self, **kwargs):
#         context = super(BookStoreList, self).get_context_data()
#         context['categories'] = Category.objects.all()
#         context['no_category_post_count'] = BookStore.objects.filter(category=None).count()
#
#         return context
#
# class BookStoreDetail(DetailView):
#     model = BookStore
#     context_object_name = 'book'
#
#     def get_context_data(self, **kwargs):
#         context = super(BookStoreDetail, self).get_context_data()
#         context['categories'] = Category.objects.all()
#         context['no_category_post_count'] = BookStore.objects.filter(category=None).count()
#
#         return context
#
# # bookregister
# def bookform_view(request):     # 폼을 통해 데이터를 입력받고 이를 데이터베이스에 저장
#     if request.method == 'POST':
#         form = BookForm_Form(request.POST, request.FILES)  # request.FILES로 폼에 입력한 사진을 데이터베이스에 저장할 수 있다.
#         if form.is_valid():
#             # 폼이 유효한 경우, 데이터 처리 로직 작성
#             form.save()  # 모델에 저장하거나 추가적인 로직 수행
#             return redirect('message_list')  # 성공 페이지로 이동
#     else:
#         form = BookForm_Form()
#
#     return render(
#         request,
#         'bookstore/templates/bookstore/bookstore_form.html',
#         {
#             'form': form,
#         }
#     )
#
# class BookForm_Form(LoginRequiredMixin, CreateView):
#     model = BookStore
#     fields = ['title', 'author', 'publisher', 'writer', 'category', 'price_set', 'price', 'img_file', 'content', 'traces', 'status']
#
#
#
#
#     def form_valid(self, form):  # 올바른 메서드 이름으로 수정
#         current_user = self.request.user
#         if current_user.is_authenticated:
#             form.instance.writer = current_user
#             return super(BookForm_Form, self).form_valid(form)
#         else:
#             return redirect('/bookstore/bookstore_list')
#
#
#
#     def form_valid(self, form):
#         current_user = self.request.user
#         if current_user.is_authenticated:
#             form.instance.writer = current_user
#             return super(BookForm_Form, self).form_valid(form)
#         else:
#             return redirect('/bookstore/bookstore_list')
#
#
#
#
# def category_page(request, slug):
#     category = Category.objects.get(slug=slug)
#     book_list = BookStore.objects.filter(category=category)
#
#     return render(
#         request,
#         'bookstore/bookstore_list.html',
#         {
#             'book_list' : book_list,
#             'categories' : Category.objects.all(),
#             'no_category_post_count':BookStore.objects.filter(category=None).count(),
#             'category':category,
#         }
#     )