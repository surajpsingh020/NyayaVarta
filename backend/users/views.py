from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm
from .utils import generate_otp, send_otp_email

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user_profile = new_user.userprofile
            user_profile.language_preference = form.cleaned_data.get('language_preference')
            otp = generate_otp()
            user_profile.otp = otp
            user_profile.is_email_verified = False
            user_profile.save()
            send_otp_email(new_user.email, otp)
            messages.success(request, "An OTP has been sent to your registered mail.")
            login(request, new_user)
            return redirect('users:verify_otp')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def verify_otp(request):
    """
    View where the user enters the OTP sent to their email.
    If correct, their email is marked as verified and they are redirected to the home page.
    """
    error = None
    if request.method == 'POST':
        otp_input = request.POST.get('otp')
        user_profile = request.user.userprofile
        if user_profile.otp == otp_input:
            user_profile.is_email_verified = True
            user_profile.otp = ""
            user_profile.save()
            return redirect('content_management:home')
        else:
            error = "Invalid OTP. Please try again."
    return render(request, 'users/verify_otp.html', {'error': error})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('content_management:home')
    else:
        form = AuthenticationForm(request)
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('users:login')
