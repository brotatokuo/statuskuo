from django.contrib import admin
from .models import BookingRequest


@admin.register(BookingRequest)
class BookingRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'photography_type', 'event_date', 'created_at']
    list_filter = ['photography_type', 'event_date', 'created_at']
    search_fields = ['name', 'email', 'location']
    readonly_fields = ['created_at']
    ordering = ['-created_at']