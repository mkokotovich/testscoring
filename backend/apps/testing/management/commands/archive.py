from datetime import timedelta

from django.core.management.base import BaseCommand
from django.utils import timezone

from apps.testing.models import Test


class Command(BaseCommand):
    help = 'Archives tests that are older than 14 days'

    def handle(self, *args, **options):
        fourteen_days = timezone.now() - timedelta(days=14)
        old_tests = Test.objects.filter(created_at__lte=fourteen_days, archived_items=[])
        for test in old_tests:
            test.archive_items()
        self.stdout.write(self.style.SUCCESS(f'Successfully archived {old_tests.count()} tests'))
