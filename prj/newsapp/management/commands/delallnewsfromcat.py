from django.core.management.base import BaseCommand, CommandError
from newsapp.models import News, Category


class Command(BaseCommand):
    help = 'Команда позволяет удалить все новости из выбранной категории'  # показывает "python manage.py <команда> --help"
    missing_args_message = 'Укажите название категории через пробел просле ввода команды' \
                           ''

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы правда хотите удалить все статьи в категории {options["category"]}? yes/no  ')
        if answer == 'yes':
            try:
                category = Category.objects.get(name=options['category'])
                News.objects.filter(category=category).delete()
                self.stdout.write(self.style.SUCCESS(f'Все новости в категории {category.name} успешно удалены'))

            except category.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Не удалось найти категорию {category}'))
        else:
            self.stdout.write(self.style.ERROR('Отменено'))


