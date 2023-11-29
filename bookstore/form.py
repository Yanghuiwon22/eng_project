from django import forms
from .models import BookStore

from .models import BookStore

class BookForm_Form(forms.ModelForm):
    class Meta:
        model = BookStore
        fields = ['title', 'author', 'publisher', 'traces', 'status','img_file','price', 'content']  # 필요한 필드들을 지정

    img_file = forms.ImageField()







