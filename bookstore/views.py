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

