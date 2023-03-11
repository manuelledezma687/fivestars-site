from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Booking, Contact, Rating, Referral, Faq


class BookingAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        try:
            old_obj = Booking.objects.get(pk=obj.pk)
            old_status = old_obj.status
        except Booking.DoesNotExist:
            old_status = None

        super().save_model(request, obj, form, change)

        if old_status == 'Pending' and obj.status == 'Confirmed':
            context = {'obj': obj}
            message = render_to_string('template_cancellation_trip.html', context)

            subject = 'Confirmation'
            recipient_list = [obj.email]
            send_mail(subject, message,  recipient_list)

        elif old_status == 'Pending' and obj.status == 'Cancelled':
            context = {'obj': obj}
            message = render_to_string('template_cancellation_trip.html', context)

            subject = 'Cancellation'
            recipient_list = [obj.email]
            send_mail(subject, message,  recipient_list)

    def has_delete_permission(self, request, obj=None):
        return True  ## False on prod

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'message')

admin.site.register(Referral)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Rating)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Faq)

