from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='lemanove@gmail.com',
            first_name='Evgeniia',
            last_name='Lemanova',
            telegram_user_name="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        user.set_password('12345678')
        user.save()

        user = User.objects.create(
            email="test@gmail.com",
            first_name="test@gmail.com",
            last_name="test@gmail.com",
            telegram_user_name="@poteryashka5",
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        user.set_password("test")
        user.save()