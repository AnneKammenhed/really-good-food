from django.db import models
from django.utils import timezone
from django.urls import reverse
from datetime import date


# class for guest
class Guest(models.Model):
    guest_name = models.CharField(max_length=25,
        verbose_name='Guest Name', blank=True,)

    guest_email = models.EmailField(verbose_name='Email',
        blank=False)

    guest_phone = models.CharField(max_length=25,
        verbose_name='Phone', blank=True)

    def __str__(self):
        return self.guest_name



# model for 1 guest to book an available table:
class Booking(models.Model):
    guest_who_books = models.ForeignKey(Guest, on_delete=models.CASCADE, null = True)
    guests_per_booking = models.PositiveSmallIntegerfield(default=2, max_value=8) 

    created_date = models.DateTimeField(default=timezone.now())
    booking_day = models.DateField(null=True)
    booking_time = models.TimeField(Null=True)
    booking_number = models.CharField(max_length=50,unique=True)

    class Meta:
        ordering = ('booking_day', 'booking_time')
        unique_together = ('guest_who_books', 'booking_day', 'booking_time')
    
    def __str__(self):
        return self.booking_number

    def save(self, **kwargs):
        if not self.booking_number:
            self.booking_number = f'{self.booking_day:%Y%m%d}{self.booking_time:%H%M}'
        super().save(**kwargs)
    
    def get_booking_url(self):
        return reverse('booktable:detail', kwargs={'pk':self.pk})

    @property
    def places_left(self):
        
        return 3