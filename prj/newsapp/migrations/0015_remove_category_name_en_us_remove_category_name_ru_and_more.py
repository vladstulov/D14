# Generated by Django 4.1.6 on 2023-03-08 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0014_category_name_en_us_category_name_ru_news_text_en_us_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en_us',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text_en_us',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en_us',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
    ]