# Generated by Django 4.1.6 on 2023-02-11 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_remove_news_category_delete_newscategory_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
