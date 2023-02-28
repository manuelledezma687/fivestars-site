from django.contrib import admin
from .models import Booking, Contact, Rating, Referral, Faq

admin.site.register((Booking, Contact, Rating, Referral, Faq))


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', "message")
