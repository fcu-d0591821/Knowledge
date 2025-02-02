from django.conf import settings
from django.core.management.base import BaseCommand
from ...models import ExtendUser
import os

class Command(BaseCommand):

    def handle(self, *args, **options):
        if ExtendUser.objects.count() == 0:
            email = os.environ.get('ADMIN_EMAIL')
            username = os.environ.get('ADMIN_USERNAME')
            password = os.environ.get('ADMIN_PASSWORD')
            print('Creating account for %s (%s)' % (username, email))
            admin = ExtendUser.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
            print('Create success')
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
