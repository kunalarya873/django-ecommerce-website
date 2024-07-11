from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from base.emails import send_account_activation_email  # Make sure this imports correctly
from .models import Profile

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(email=email).first()
        
        if not user_obj:
            messages.warning(request, "User doesn't exist")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = authenticate(username=email, password=password)
        
        if user_obj:
            if not user_obj.profile.is_email_verified():
                messages.warning(request, "Email not verified")
                return HttpResponseRedirect(request.path_info)
            
            login(request, user_obj)
            messages.success(request, 'You are logged in')
            return redirect('/')
        else:
            messages.warning(request, 'Invalid credentials')
        
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email).first()

        if user_obj:
            messages.warning(request, "User already exists")
            return HttpResponseRedirect(request.path_info)
        
        user_obj = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
            password=password
        )
        
        profile = Profile.objects.create(user=user_obj, is_email_verified=False)
        
        # Generate token
        email_token = default_token_generator.make_token(user_obj)
        
        # Send activation email
        send_account_activation_email(email, email_token)
        
        
        messages.success(request, 'Message is sent to your email for verification')
        return redirect('login_page')  # Redirect to the login page after registration
    
    return render(request, 'register.html')
