from django.core.management.base import BaseCommand, CommandError
from stuf.exporta import run
import traceback


class Command(BaseCommand):
    help = 'Exports material to md files'

    def handle(self, *args, **options):
        try:
            run()
        except Exception as e:
            traceback.print_exc()
            raise CommandError(f"Error exportant: {e}")

        self.stdout.write(self.style.SUCCESS(
            "Exportació finalitzada"))
