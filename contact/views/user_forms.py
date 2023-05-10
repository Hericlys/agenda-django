from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm

from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):

    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'successfully user registered')
            form.save()
            return redirect('contact:login')
            
    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )

def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'login successfully')
            return redirect('contact:index')

        messages.error(request, 'login failed')

    return render(
        request,
        'contact/login.html',
        {
            'form': form
        }
    )

def logout_view(request):
    auth.logout(request)
    return redirect('contact:login')

def user_update(request):

    form = RegisterUpdateForm(instance=request.user)

    if request.method == 'POST':

        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'update successful')
            return redirect('contact:user_update')

    return render(
        request,
        'contact/user_update.html',
        {
            'form': form
        }
    )