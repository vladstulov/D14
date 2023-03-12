from django.contrib import admin
from .models import News, Category
from modeltranslation.admin import TranslationAdmin

from datetime import datetime
import datetime

class CategoryAdmin(TranslationAdmin):
    model = Category
class NewsAdmin(TranslationAdmin):
    model = News



def updt_dateCreat(modeladmin, request, queryset):
    # queryset — грубо говоря набор объектов, которых мы выделили галочками.
    queryset.update(dateCreation=datetime.datetime.now())
updt_dateCreat.short_description = 'Обновить дату создания поста' # описание для более понятного представления в админ панеле задаётся, как будто это объект

class NewsAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in News._meta.get_fields()] # генерируем список имён всех полей для более
    list_display = ('id', id, 'title', 'text', 'length_text_gt_200_symb', 'dateCreation', 'category')  # оставляем только имя и цену товара
    list_filter = ('category__name','id', 'title', 'dateCreation')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'text')

    actions = [updt_dateCreat]


class CategoryAdmin(admin.ModelAdmin):
    #list_display = [field.name for field in Category._meta.get_fields()] # генерируем список имён всех полей для более
    list_display = ('id', id, 'name',)
    list_filter = ('id', 'name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
#admin.site.register(NewsCategory)

#admin.site.unregister(Category)
