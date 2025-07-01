from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingRequestForm
from .models import BookingPage


def booking_view(request):
    if request.method == 'POST':
        form = BookingRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your booking request has been submitted. We will contact you soon.')
            return redirect('booking')
    else:
        form = BookingRequestForm()
    
    try:
        booking_page = BookingPage.objects.live().first()
    except BookingPage.DoesNotExist:
        booking_page = None
    
    return render(request, 'home/booking_page.html', {
        'form': form,
        'page': booking_page,
    })