from django.core.management.base import BaseCommand
from wagtail.models import Site
from home.models import HomePage, GraduationPage, WeddingPage, PersonalPage, BookingPage


class Command(BaseCommand):
    help = 'Set up photography pages (Graduation, Wedding, Personal, Booking)'

    def handle(self, *args, **options):
        try:
            site = Site.objects.get(is_default_site=True)
            homepage = site.root_page.specific
            
            if not isinstance(homepage, HomePage):
                self.stdout.write(
                    self.style.ERROR('Homepage is not set up properly. Run setup_homepage first.')
                )
                return

            # Create Graduation Page
            if not GraduationPage.objects.filter(slug='graduation').exists():
                graduation_page = GraduationPage(
                    title='Graduation Photography',
                    slug='graduation',
                    intro='<p>Celebrate your academic achievements with professional graduation photography. Capture this milestone moment with beautiful, high-quality photos that you\'ll treasure forever.</p>'
                )
                homepage.add_child(instance=graduation_page)
                graduation_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Created Graduation Photography page'))
            else:
                self.stdout.write('Graduation page already exists')

            # Create Wedding Page
            if not WeddingPage.objects.filter(slug='wedding').exists():
                wedding_page = WeddingPage(
                    title='Wedding Photography',
                    slug='wedding',
                    intro='<p>Your wedding day is one of the most important days of your life. Let us capture every precious moment with our professional wedding photography services, creating timeless memories that will last a lifetime.</p>'
                )
                homepage.add_child(instance=wedding_page)
                wedding_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Created Wedding Photography page'))
            else:
                self.stdout.write('Wedding page already exists')
                
            # Create Personal Page
            if not PersonalPage.objects.filter(slug='personal').exists():
                personal_page = PersonalPage(
                    title='Personal Photography',
                    slug='personal',
                    intro='<p>Whether you need professional headshots, family portraits, or personal branding photos, our personal photography services will help you look your best and tell your unique story.</p>'
                )
                homepage.add_child(instance=personal_page)
                personal_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Created Personal Photography page'))
            else:
                self.stdout.write('Personal page already exists')
                
            # Create Booking Page
            if not BookingPage.objects.filter(slug='booking').exists():
                booking_page = BookingPage(
                    title='Book Your Session',
                    slug='booking',
                    intro_text='<p>Ready to book your photography session? Fill out the form below with your details and we\'ll get back to you within 24 hours to discuss your needs and schedule your session.</p><p><strong>What to expect:</strong></p><ul><li>Quick response within 24 hours</li><li>Free consultation to discuss your vision</li><li>Flexible scheduling to fit your needs</li><li>Professional, high-quality results</li></ul>'
                )
                homepage.add_child(instance=booking_page)
                booking_page.save_revision().publish()
                self.stdout.write(self.style.SUCCESS('✅ Created Booking page'))
            else:
                self.stdout.write('Booking page already exists')
                
            self.stdout.write(
                self.style.SUCCESS(
                    '\n🎉 Photography site setup complete!\n'
                    'Visit your site to see:\n'
                    '• Homepage with navigation to all sections\n'
                    '• Graduation Photography gallery\n'
                    '• Wedding Photography gallery\n'
                    '• Personal Photography gallery\n'
                    '• Booking request form\n\n'
                    'Admin users can add photos to galleries at /admin/\n'
                    'Booking requests can be viewed at /django-admin/home/bookingrequest/'
                )
            )
            
        except Site.DoesNotExist:
            self.stdout.write(
                self.style.ERROR('No default site found. Please create a site first.')
            )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error setting up pages: {e}')
            )