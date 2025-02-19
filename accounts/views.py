from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, LoginForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.constants.SUCCESS, 'Conta Cadastrada!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_type == 'provider':
                    return redirect('provider_interface')
                else:
                    return redirect('user_interface')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def provider_interface(request):
    return render(request, 'services/my_services.html')

def user_interface(request):
    return render(request, 'accounts/user_interface.html')

def homepage(request):
    return render(request, 'accounts/homepage.html')

