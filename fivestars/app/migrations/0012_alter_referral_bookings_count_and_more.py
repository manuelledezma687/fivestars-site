# Generated by Django 4.1.7 on 2023-03-06 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_rename_bookings_amount_booking_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referral',
            name='bookings_count',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='referral',
            name='earnings',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=8),
        ),
    ]
