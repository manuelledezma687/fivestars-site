from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from .models import Rating, Faq, Referral
from .forms import ContactForm, BookingForm, CustomAuthenticationForm


def index(request):
    ratings = Rating.objects.order_by('-created_at')[:3]
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['referrals_code']
            results = Referral.objects.filter(campo__icontains=query)
            form.save()
            return redirect('app:success')
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
            form.save()
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
