from django import forms
from .models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('title', 'author', 'price', 'pages', 'book_type', 'publication_date')
