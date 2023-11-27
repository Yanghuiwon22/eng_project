from django import forms
from .models import BookStore

from .models import BookStore

class BookForm_Form(forms.ModelForm):
    class Meta:
        model = BookStore
        fields = ['title', '지은이', '출판사', '필기흔적', '보존상태','img_file','희망가격']  # 필요한 필드들을 지정

