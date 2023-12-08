from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания пользователя"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='artem.matrashov@yandex.ru',
                                   first_name='Artem',
                                   last_name='Testov',
                                   is_staff=False,
                                   is_superuser=False)

        user.set_password('admin')
        user.save()
