from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Contact, Booking, PAYMENT_METHOD, SERVICES, PASSENGERS


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('full_name', 'email', "message")


class BookingForm(forms.ModelForm):
    pick_up_location = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Type your location',
        'autofocus': 'autofocus',
        'class': 'form-control', }))
    drop_off_location = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'placeholder': 'Type your location',
        'autofocus': 'autofocus',
        'class': 'form-control', }))
    full_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder': 'Full Name',
        'autofocus': 'autofocus',
        'class': 'form-control',
    }))
    email = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
        'placeholder': 'youremail@example.com',
        'type': 'email',
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    hour = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': 'time',
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    date = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'type': 'date',
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    flight_id = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Flight Number',
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD, widget=forms.Select(attrs={
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    passengers = forms.ChoiceField(choices=PASSENGERS, widget=forms.Select(attrs={
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'placeholder': 'Your phone',
        'autofocus': 'autofocus',
        'class': 'form-control'}))
    observations = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Observations',
        'autofocus': 'autofocus',
        'class': 'form-control', }))
    referrals = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Referral Code 10% OFF DISCOUNT',
        'autofocus': 'autofocus',
        'class': 'form-control', }))
    type_of_service = forms.ChoiceField(choices=SERVICES, widget=forms.Select(attrs={
        'autofocus': 'autofocus',
        'class': 'form-control', }))

    class Meta:
        model = Booking
        fields = ('pick_up_location', 'drop_off_location', "full_name",
                  'email', 'hour', 'date', 'flight_id', 'payment_method', 'passengers', 'phone', 'observations', 'referrals', 'type_of_service')


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Usuario'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))
