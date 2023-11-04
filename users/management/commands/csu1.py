from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания суперпользователя"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='moder@sky.pro',
                                   first_name='Andrey',
                                   last_name='Matrashov',
                                   is_staff=True,
                                   is_superuser=True)

        user.set_password('moder')
        user.save()
