from django import forms
from django.utils import timezone
from models import Guest, Booking


SEATING_TIMES = ['17h:00', '18h:30', '20h:00']

class BookingForm(forms.ModelForm):


# is there an available time?
    available_time = check_free_time(SEATING_TIMES, today_time_slot)
    if available_time:
        message = f'We are fully booked at this time, please choose another time in {available_slot}'
        raise forms.ValidationError(message)
    else:
        message = 'Sorry, there are no available times today.'
        raise forms.ValidationError(message)
