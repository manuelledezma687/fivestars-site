from django.db import models
import secrets


SERVICES = (
    ("O", "Type of Service"),
    ("Hourly", "Hourly"),
    ("One way", "One way"),
)

PASSENGERS = (
    ("O", "Passengers"),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
)

PAYMENT_METHOD = (
    ("O", "Payment Method"),
    ("Cash", "Cash"),
    ("Zelle", "Zelle"),
)


class Referral(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50, unique=True)
    referrals_code = models.CharField(max_length=8, unique=True, editable=False)
    created_at = models.DateTimeField("date created")

    def __str__(self):
        columns = f"{self.full_name} | {self.email} | {self.referrals_code}"
        return columns

    def save(self, *args, **kwargs):
        if not self.referrals_code:
            self.referrals_code = self.generate_code()
        super().save(*args, **kwargs)

    def generate_code(self):
        code = secrets.token_hex(4)[:8]
        while Referral.objects.filter(referrals_code=code).exists():
            code = secrets.token_hex(4)[:8]
        return code

class Booking(models.Model):
    type_of_service = models.CharField(
        max_length=20, choices=SERVICES, default=None)
    pick_up_location = models.CharField(max_length=150)
    drop_off_location = models.CharField(max_length=150)
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    hour = models.CharField(max_length=30, default=None)
    date = models.CharField(max_length=30, default=None)
    flight_id = models.CharField(max_length=20)
    payment_method = models.CharField(
        max_length=20, choices=PAYMENT_METHOD, default=None)
    passengers = models.IntegerField(choices=PASSENGERS, default=None)
    phone = models.CharField(max_length=20)
    observations = models.CharField(max_length=200, blank=True)
    referrals_code = models.CharField(max_length=8, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        colmuns = f'Referral Code: ' + self.referrals_code + ' |'+ self.full_name + ' | ' + self.pick_up_location + ' To ' + \
            self.drop_off_location + ' | ' + self.email + ' | ' + self.phone
        return colmuns


class Rating(models.Model):
    booking_id = models.OneToOneField(Booking, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    comments = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        colmuns = f'' + self.first_name + ' ' + \
            self.last_name + ' | ' + self.comments
        return colmuns


class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        colmuns = f'' + self.email + ' | Message:' + \
            self.message + ' | ' + self.full_name
        return colmuns


class Faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)

    def __str__(self):
        colmuns = f'  ' + self.question
        return colmuns
