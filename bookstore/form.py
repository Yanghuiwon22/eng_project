from django import forms
from .models import BookStore

from .models import BookForm_Mod

class BookForm_Form(forms.ModelForm):
    class Meta:
        model = BookForm_Mod
        fields = ['책_이름','지은이','출판사','필기흔적']  # 필요한 필드들을 지정

