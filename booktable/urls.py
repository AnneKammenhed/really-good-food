from django.urls import path
from booktable import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('bookings', views.add_booking, name='bookings'),
    path('get_booking', views.get_booking, name='get_booking')
]
