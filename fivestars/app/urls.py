from django.urls import path
from . import views

app_name = 'app'

handler404 = views.not_found

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name='login'),
    path("bookings", views.bookings, name="bookings"),
    path("contact", views.contact, name="contact"),
    path("success", views.success, name="success"),
    path("success_message", views.success_message, name="success_message"),
    path('privacy', views.privacy, name='privacy'),
    path('faqs', views.faqs, name='faqs'),
]
