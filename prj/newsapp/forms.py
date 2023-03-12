from django.forms import ModelForm
from .models import News, Category

from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as __

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'author', 'category']
        labels = {
            'title': __('Title'),
            'text': __('Text'),
            'author': __('Author'),
            'category': __('Category'),
        }