from django.urls import path
from booktable import views

urlpatterns = [
    path('', views.home, name="home"),
    path('menu', views.menu, name="menu"),
    path('bookings', views.add_booking, name='bookings'),
]
