from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Rating, Faq, Contact, Referral
from .forms import ContactForm, BookingForm, CustomAuthenticationForm


def index(request):
    ratings = Rating.objects.order_by('-created_at')[:3]
    today = datetime.today().date()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            referral_code = form.cleaned_data.get('referrals_code')
            booking = form.save(commit=False)
            if referral_code:
                try:
                    referral = Referral.objects.get(
                        referrals_code=referral_code)
                    booking.referrals_code = referral
                except Referral.DoesNotExist:
                    return render(request, 'home.html', {'form': form, 'error': 'Referral code does not exist.'})
            form.save()
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            pick_up_location = form.cleaned_data['pick_up_location']
            drop_off_location = form.cleaned_data['drop_off_location']
            subject = f'Booking from {full_name}'
            html_content = render_to_string('template_email_booking_client.html', {
                                            'full_name': full_name, 'email': email, 'phone': phone, 'pick_up_location': pick_up_location, 'drop_off_location': drop_off_location})
            text_content = strip_tags(html_content)
            email_msg = EmailMultiAlternatives(subject, text_content, to=[
                                               'manuelledezma687@gmail.com'], cc=[email])
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()
            return redirect('app:success')
        else:
            context = {
                'ratings': ratings,
                'form': form,
            }
            return render(request, "home.html", context)
    else:
        form = BookingForm()
    context = {
        'ratings': ratings,
        'form': form,
    }
    return render(request, "home.html", context)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def success(request):
    return render(request, "success.html")


def success_message(request):
    return render(request, "success_message.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f'Message from {full_name}'
            html_content = render_to_string('template_email_contact.html', {
                                            'full_name': full_name, 'email': email, 'message': message})
            text_content = strip_tags(html_content)
            email_msg = EmailMultiAlternatives(subject, text_content, to=[
                                               'manuelledezma687@gmail.com'], cc=[email])
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()
            contact = Contact(full_name=full_name,
                              email=email, message=message)
            contact.save()
            return redirect('app:success_message')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('app:index')
            else:
                form.add_error(None, 'Invalid user or password')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login_admin.html', {'form': form})


def privacy(request):
    return render(request, "privacy.html")


def faqs(request):
    faqs = Faq.objects.all()
    return render(request, "faqs.html", {'faqs': faqs})
