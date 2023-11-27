from django import forms
from .models import BookStore

from .models import MyCustomModel

class MyCustomForm(forms.ModelForm):
    class Meta:
        model = MyCustomModel
        fields = ['field1', 'field2']  # 필요한 필드들을 지정

