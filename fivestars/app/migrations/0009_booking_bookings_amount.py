# Generated by Django 4.1.7 on 2023-03-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_booking_referrals_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bookings_amount',
            field=models.FloatField(default=0),
        ),
    ]