from django.core.management import BaseCommand
from django.core.management.utils import get_random_secret_key


class Command(BaseCommand):
    help = "Create environment variables"

    def add_arguments(self, parser):
        parser.add_argument(
            "--sentry-dsn",
            "-dsn",
            dest="DSN",
            type=str,
            help="Specify the Sentry DSN URL",
        )
        parser.add_argument(
            "--host-url",
            "-host",
            dest="HOST",
            type=str,
            help="Specify the URL to add in ALLOWED_HOSTS",
        )

    def handle(self, *args, **options):
        with open('.env', 'w') as f:
            f.write(f'DJANGO_SECRET_KEY={get_random_secret_key()}\n')
            f.write(f'SENTRY_DSN={options["DSN"]}\n')
            f.write(f'HOST_URL={options["HOST"]}\n')
            f.close()
