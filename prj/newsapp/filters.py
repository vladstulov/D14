from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFilter
from django.forms import DateInput, TextInput
from .models import News, Category, User

from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy as __

from django.db import models
class NewsFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        label=__('Title'),
        lookup_expr=__('icontains'),
    )

    text = CharFilter(
        field_name='text',
        label=__('Text'),
        lookup_expr=__('icontains'),
    )

    author = ModelChoiceFilter(
        field_name='author',
        queryset=User.objects.all(),
        label=__('Author'),
        empty_label=__('select authors'),
    )

    dateCreation = DateFilter(
        field_name='dateCreation',
        label=__('Date creation'),
        lookup_expr=__('gte'),
        widget=DateInput(
            format='%Y-%m-%dT',
            attrs={'type': 'date'},
        ),
    )

    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label=__('Category'),
        empty_label=__('select category')
    )

#Пришлось изменить, на то как выше, чтобы работали переводы полей поиска

# from django_filters import FilterSet
# from .models import News, Category
# class NewsFilter(FilterSet):
#    class Meta:
#         model = News
#         fields = {
#             'title': ['icontains'],
#             'dateCreation' : ['lt'],
#             'text': ['icontains'],
#             'author': ['in'],
#             'category': ['in'],
#         }




