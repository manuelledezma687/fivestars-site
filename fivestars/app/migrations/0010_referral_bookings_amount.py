# Generated by Django 4.1.7 on 2023-03-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_booking_bookings_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='bookings_amount',
            field=models.FloatField(default=0),
        ),
    ]
