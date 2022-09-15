from django.urls import path
from booktable import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('bookings', views.add_booking, name='bookings'),
    path('booking_list', views.get_booking, name='booking_list'),
    path('edit_booking/<booking_id>', views.edit_booking, name='edit-booking'),
    path('delete_booking/<booking_id>', views.delete_booking, name='delete-booking'),
]
