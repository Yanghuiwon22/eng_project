from django import forms
from .models import BookStore

from .models import BookForm_Mod

class BookForm_Form(forms.ModelForm):
    class Meta:
        model = BookForm_Mod
        fields = ['field1', 'field2', 'bookname']  # 필요한 필드들을 지정

