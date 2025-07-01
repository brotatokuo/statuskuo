from django import forms
from .models import BookingRequest


class BookingRequestForm(forms.ModelForm):
    class Meta:
        model = BookingRequest
        fields = ['name', 'email', 'phone', 'photography_type', 'event_date', 'location', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number (optional)'}),
            'photography_type': forms.Select(attrs={'class': 'form-control'}),
            'event_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Location'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4, 
                'placeholder': 'Tell us more about your photography needs...'
            }),
        }