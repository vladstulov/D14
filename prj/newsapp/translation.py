from .models import Category, News
from modeltranslation.translator import register, TranslationOptions  # импортируем декоратор для перевода и класс настроек,
# от которого будем наследоваться


# регистрируем наши модели для перевода

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # указываем, какие именно поля надо переводить в виде кортежа


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title','text', 'category')