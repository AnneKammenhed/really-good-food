from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect

from django.db import models
from django import forms
from django.forms import ModelForm

from .models import Booking, Menu
from .forms import BookingForm

# from django.urls import reverse
# from django.views.generic.edit import FormView


# function to add valid bookings to the database
def add_booking(request):
    submitted = False
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return HttpResponseRedirect('bookings?submitted=True')
    else:
        booking_form = BookingForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'bookings.html', {'form': booking_form, 'submitted': submitted})


# functions to show, edit and delete own booking
def get_booking(request):
    booking_list = Booking.objects.filter(guest=request.user)
    return render(request, 'booking_list.html', {'booking_list': booking_list})

def edit_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    form = BookingForm(request.POST or None, instance=booking)
    return render(request, 'edit_booking.html', {'booking': booking, 'form': form})

def delete_booking(request, booking_id):
    booking = Booking.objects.get(pk=booking_id)
    if request.user.is_user:
        booking.delete()
        return redirect('booking_list')


def home(request):
    return render(request, 'index.html')


def menu(request):
    menu = Menu.objects.all()
    return render(request, 'menu.html', {'menu': menu})
