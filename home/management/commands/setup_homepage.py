from django.core.management.base import BaseCommand
from wagtail.models import Site
from home.models import HomePage


class Command(BaseCommand):
    help = 'Set up the homepage with default content for non-technical users'

    def handle(self, *args, **options):
        try:
            site = Site.objects.get(is_default_site=True)
            homepage = site.root_page.specific
            
            if isinstance(homepage, HomePage):
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Homepage is already set up! You can edit it at: /admin/pages/{homepage.id}/'
                    )
                )
                self.stdout.write(
                    'Current content:\n'
                    f'  Hero Title: {homepage.hero_title}\n'
                    f'  About Title: {homepage.about_title}\n'
                    f'  Contact Email: {homepage.contact_email or "Not set"}\n'
                    f'  Contact Phone: {homepage.contact_phone or "Not set"}'
                )
                return
                
            # If not a HomePage, create one
            self.stdout.write('Creating new HomePage...')
            new_homepage = HomePage(
                title='Home',
                slug='home',
                hero_title='Welcome to StatusKuo Photography',
                hero_subtitle='Capturing life\'s perfect moments',
                about_title='About Our Photography',
                about_text='<p>We specialize in creating beautiful, timeless photographs that tell your story. From portraits to events, we capture the moments that matter most.</p>',
                contact_email='info@statuskuo.com'
            )
            
            # Add as child of root and set as homepage
            site.root_page.add_child(instance=new_homepage)
            site.root_page = new_homepage
            site.save()
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'Homepage created successfully! Edit it at: /admin/pages/{new_homepage.id}/'
                )
            )
            
        except Site.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('No default site found. Please create a site first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error setting up homepage: {e}')
            )