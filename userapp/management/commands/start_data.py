from django.core.management import BaseCommand

from userapp.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_superuser(username='admin',
                                      email='admin@mail.ru',
                                      password='123')
        self.test_data_users()

    @staticmethod
    def test_data_users():
        User.objects.create(username='BalabanovIvan123',
                            last_name='Иван',
                            first_name='Балабанов',
                            email='balabanov@mail.ru',
                            password='123123123qw')

        User.objects.create(username='PugachevAndry123',
                            last_name='Андрей',
                            first_name='Пугачев',
                            email='pugachev@mail.ru',
                            password='123123123qw')

        User.objects.create(username='RybovSergey123',
                            last_name='Сергей',
                            first_name='Рыбов',
                            email='rybov@mail.ru',
                            password='123123123qw')
