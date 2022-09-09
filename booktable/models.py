from django.db import models

# restaurant is open Tuesday to Saturday
OPENING_DAYS = (
    (0, 'Tuesday'),
    (1, 'Wednesday'),
    (2, 'Thursday'),
    (3, 'Friday'),
    (4, 'Saturday'),
)

# restaurant has three seatings
SEATING_TIMES = (
    (0, '17:00-18:30'),
    (1, '18:30-20:00'),
    (2, '20:00-21:30'),
)

# each online booking is for max eight guests
GUESTS_PER_BOOKING = (
    (0, 'Table for one'),
    (1, 'Table for two'),
    (2, 'Table for three'),
    (3, 'Table for four'),
    (4, 'Table for five'),
    (5, 'Table for six'),
    (6, 'Table for seven'),
    (7, 'Table for eight'),
)

# each seating has max 80 guests NUMBER_OF_GUESTS at OPENING_DAY&SEATING_TIME=80
MAX_GUESTS = (
    (80, 'Restaurant is fully booked'),
)
# 52 weeks

# class for guest
class Guest(models.Model):
    guest_name = models.CharField(max_length=25,
        verbose_name='Guest Name', blank=True,)

    guest_email = models.EmailField(verbose_name='Email',
        blank=False)

    guest_phone = models.CharField(max_length=25,
        verbose_name='Phone', blank=True)

    def __str__(self):
        return f'{self.guest_name}'



# model for 1 guest to book an available table:
class Booking(models.Model):
    guest_who_books = models.ForeignKey(Guest, on_delete=models.CASCADE,
       related_name=guest_booking)
    guests_per_booking = models.Integerfield(choices=GUESTS_PER_BOOKING, db_index=True) 
    booking_day = models.Integerfield(choices=OPENING_DAYS, db_index=True)
    booking_time = models.Integerfield(choices=SEATING_TIMES, db_index=True)

    class Meta:
        ordering = ('booking_day', 'booking_time')
        unique_together = ('guest_who_books', 'booking_day', 'booking_time')
    
    def __str__(self):
        return f'{self.guest_who_books} for {self.number_of_guests} at
        {self.booking_day}{self.booking_time}'


# if time is unavailable
class UnavailableTimes(Exception):
    pass


# class for available times
class AvailableTimes(models.Model):
    BOOKED = 0
    AVAILABLE = 1
    STATUS_BOOKINGS = [
        (BOOKED, "Booked"),
        (AVAILABLE, "Available"),
    ]

    available_times = models.BooleanField(choices=STATUS_BOOKINGS)
    seating = models.DateTimeField(choices=SEATING_TIMES, unique_together=OPENING_DAYS, SEATING_TIMES, MAX_GUESTS)
    status = models.IntegerField(choices = STATUS_BOOKINGS, default = AVAILABLE)
