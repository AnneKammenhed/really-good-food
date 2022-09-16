import unittest
from django.test import TestCase
from .models import Booking


# class to test Booking model
class TestAddBooking(unittest.TestCase):
    # test to se that closed day Sunday fails
    # def test_booking_day(self):
    #    booking = Booking('Sun')
    #
    #    self.assertEqual(booking.booking_day, 'Sun')

    # test to se that open day Tuesday passes
    def test_booking_day(self):
        booking = Booking('Tue')

        self.assertEqual(booking.booking_day, 'Tue')

if __name__ == '__main__':
    unittest.main()
