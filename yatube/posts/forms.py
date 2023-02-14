from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        # это и есть проверка. Если данные ничего не содержат - выдаем ошибку
        if data == '':
            raise forms.ValidationError('Поле не заполнено')
        return data
