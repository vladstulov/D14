from django.db import models
from django.contrib.auth.models import User

import datetime
from datetime import timedelta
from datetime import datetime

from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy # импортируем «ленивый» геттекст с подсказкой

class Category(models.Model):
    objects = None

    name = models.CharField(max_length=64, unique=True, help_text = _('Category name'))
    subscribers = models.ManyToManyField(User, related_name='categories', blank=True, help_text = _('Subscribers category'))
    def __str__(self):
        return self.name
class News(models.Model):
    #title = models.CharField(max_length=50, unique=True, help_text = _('Title'))
    title = models.CharField(max_length=50, unique=True, verbose_name = pgettext_lazy('help text for title','Title'))
    text = models.TextField( help_text = _('Text article'))
    dateCreation = models.DateTimeField(auto_now_add=True, help_text = _('Date creation'))
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='author', help_text = _('Author'))
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='category', help_text = _('Category name'))
    #category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='category',
                                 #verbose_name=pgettext_lazy('help text for MyModel model. Field Category', 'This is the test help text. Field Category'))

    @property
    def length_text_gt_200_symb(self):
        return len(self.text) > 200
    def preview(self):
        preview = f'{self.text[:124]} ...'
        return preview

    def __str__(self):
        return f'{self.title.title()}. Дата публикации: {self.dateCreation.strftime("%d %B, %Y")}. {self.text[:50]}...'
    def get_absolute_url(self):
        return f'/news/{self.id}'

