# Generated by Django 4.1.7 on 2023-02-28 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_service', models.CharField(choices=[('Hourly', 'Hourly'), ('One way', 'One way')], default=None, max_length=20)),
                ('pick_up_location', models.CharField(max_length=150)),
                ('drop_off_location', models.CharField(max_length=150)),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('hour', models.CharField(default=None, max_length=30)),
                ('date', models.CharField(default=None, max_length=30)),
                ('flight_id', models.CharField(max_length=20)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Zelle', 'Zelle')], default=None, max_length=20)),
                ('passengers', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=None)),
                ('phone', models.CharField(max_length=20)),
                ('observations', models.CharField(blank=True, max_length=200)),
                ('referral', models.CharField(blank=True, max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=20)),
                ('referrals_code', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.booking')),
            ],
        ),
    ]
