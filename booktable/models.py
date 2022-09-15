from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Model to book a table = available times+number of guests+guest details
class Booking(models.Model):
    # values for what days Good Food is open, three seatings:
    THISWEEK = 'Current week'
    NEXTWEEK = 'Next week'
    WEEK_CHOICES = [
        (THISWEEK, 'This week'),
        (NEXTWEEK, 'Next week'),
    ]

    TUESDAY = 'Tue'
    WEDNESDAY = 'Wed'
    THURSDAY = 'Thu'
    FRIDAY = 'Fri'
    SATURDAY = 'Sat'
    OPENING_DAYS_CHOICES = [
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),   
    ]

    DINNER1 = '17.00-18.30'
    DINNER2 = '18.30-20.00'
    DINNER3 = '20.00-21.30'
    SEATING_TIMES_CHOICES = [
        (DINNER1, '17.00-18.30'),
        (DINNER2, '18.30-20.00'),
        (DINNER3, '20.00-21.30'),
    ]

    # online booking allows for a maximum of eight guests
    ONE = 'One guest'
    TWO = 'Two guests'
    THREE = 'Three guests'
    FOUR = 'Four guests'
    FIVE = 'Five guests'
    SIX = 'Six guests'
    SEVEN = 'Seven guests'
    EIGHT = 'Eight guests'
    NUMBER_OF_GUESTS = [
        (ONE, 'One guest'),
        (TWO, 'Two guests'),
        (THREE, 'Three guests'),
        (FOUR, 'Four guests'),
        (FIVE, 'Five guests'),
        (SIX, 'Six guests'),
        (SEVEN, 'Seven guests'),
        (EIGHT, 'Eight guests'),
    ]

    booking_week = models.CharField(
        max_length=12,
        choices=WEEK_CHOICES,
        default=THISWEEK,
    )

    booking_day = models.CharField(
        max_length=10,
        choices=OPENING_DAYS_CHOICES,
        default=TUESDAY,
    )
    
    booking_time = models.CharField(
        max_length=20,
        choices=SEATING_TIMES_CHOICES,
        default=DINNER1,
    )

    booking_made = timezone.now()

    number_of_guests = models.CharField(
        max_length=20,
        choices=NUMBER_OF_GUESTS, 
        default=TWO,
    )

    allergies = models.TextField(
        max_length=100, 
        verbose_name='Allergies',
        blank=True,
    )

    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")

    objects = models.Manager()

    class Meta:
        ordering = ('booking_week', 'booking_day', 'booking_time')
        unique_together = ('guest', 'booking_week', 'booking_day', 'booking_time')

    def __str__(self):
        return f'{self.guest} for {self.number_of_guests} on {self.booking_day} at {self.booking_time}'


# Model for the menu page
class Menu(models.Model):
    STARTERS = 'Starters'
    MAINS = 'Main courses'
    DESERTS = 'Deserts'
    COURSES = [
        (STARTERS, 'Starters'),
        (MAINS, 'Main courses'),
        (DESERTS, 'Deserts'),
    ]
    
    course_type = models.CharField(
        max_length=12,
        choices=COURSES,
        default=MAINS,
    )

    course_image = CloudinaryField('image', default='placeholder')

    course_name = models.CharField(max_length=25, unique=True, default="")

    course_description = models.CharField(max_length=100, unique=False, default="")

    class Meta:
        ordering = ('course_type', 'course_image', 'course_name', 'course_description')

    def __str__(self):
        return f'{self.course_name}'
