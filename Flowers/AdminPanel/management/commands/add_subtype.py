from django.core.management.base import BaseCommand
from AdminPanel.models import Categories

class Command(BaseCommand):
    help = 'Создает категории для кнопок, сообщений и списков'

    def handle(self, *args, **options):
        categories = ["Розы", "Монобукеты", "Акция дня", "Оптовые пачки", "Общие", "Пересекающиеся"]
        for category_name in categories:
            Category.objects.get_or_create(name=category_name)
        self.stdout.write(self.style.SUCCESS('Категории успешно созданы'))
