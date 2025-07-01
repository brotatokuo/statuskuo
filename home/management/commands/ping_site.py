import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Ping statuskuo.onrender.com to keep it alive'

    def add_arguments(self, parser):
        parser.add_argument(
            '--url',
            type=str,
            default='https://statuskuo.onrender.com',
            help='URL to ping (default: https://statuskuo.onrender.com)'
        )
        parser.add_argument(
            '--timeout',
            type=int,
            default=30,
            help='Request timeout in seconds (default: 30)'
        )

    def handle(self, *args, **options):
        url = options['url']
        timeout = options['timeout']
        
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully pinged {url} - Status: {response.status_code}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Pinged {url} but got status: {response.status_code}')
                )
        except requests.exceptions.RequestException as e:
            self.stdout.write(
                self.style.ERROR(f'Failed to ping {url}: {str(e)}')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Unexpected error pinging {url}: {str(e)}')
            )