from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel


class HomePage(Page):
    # Hero section
    hero_title = models.CharField(
        max_length=255,
        default="Capturing Life's Perfect Moments",
        help_text="Main headline for the hero section"
    )
    hero_subtitle = models.CharField(
        max_length=255,
        blank=True,
        help_text="Subtitle text below the main headline"
    )
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Large hero background image"
    )
    
    # Featured work section
    featured_image_1 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="First featured photograph"
    )
    featured_image_2 = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Second featured photograph"
    )
    
    # About section
    about_title = models.CharField(
        max_length=255,
        default="About StatusKuo",
        help_text="Title for the about section"
    )
    about_text = RichTextField(
        blank=True,
        help_text="Brief description about your photography business"
    )
    
    # Contact info
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('hero_title'),
        FieldPanel('hero_subtitle'),
        FieldPanel('hero_image'),
        FieldPanel('featured_image_1'),
        FieldPanel('featured_image_2'),
        FieldPanel('about_title'),
        FieldPanel('about_text'),
        FieldPanel('contact_email'),
        FieldPanel('contact_phone'),
    ]


class PhotoGalleryImage(Orderable):
    page = ParentalKey('PhotoGalleryPage', on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )
    caption = models.CharField(max_length=250, blank=True)
    
    panels = [
        FieldPanel('image'),
        FieldPanel('caption'),
    ]


class PhotoGalleryPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]
    
    subpage_types = []


class GraduationPage(PhotoGalleryPage):
    template = 'home/photo_gallery_page.html'
    
    class Meta:
        verbose_name = "Graduation Photography Page"


class WeddingPage(PhotoGalleryPage):
    template = 'home/photo_gallery_page.html'
    
    class Meta:
        verbose_name = "Wedding Photography Page"


class PersonalPage(PhotoGalleryPage):
    template = 'home/photo_gallery_page.html'
    
    class Meta:
        verbose_name = "Personal Photography Page"


class BookingRequest(models.Model):
    PHOTOGRAPHY_TYPES = [
        ('graduation', 'Graduation'),
        ('wedding', 'Wedding'),
        ('personal', 'Personal'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    photography_type = models.CharField(max_length=20, choices=PHOTOGRAPHY_TYPES)
    event_date = models.DateField()
    location = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.photography_type} - {self.event_date}"
    
    class Meta:
        ordering = ['-created_at']


class BookingPage(Page):
    intro_text = RichTextField(
        blank=True,
        help_text="Introduction text for the booking page"
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('intro_text'),
    ]
    
    subpage_types = []