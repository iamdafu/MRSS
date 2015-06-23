from django.core.management.base import BaseCommand, CommandError
from search_engine.models import SearchWord

class Command(BaseCommand):
    help = 'test cooperation with other programms'

    def handle(self, *args, **options):
        f
