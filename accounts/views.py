from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages

def login_view(request):
    if request.user.is_authenticated:
        return redirect('tenis_list')  

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}!")
            return redirect('tenis_list')

    else:
        form = AuthenticationForm(request)

    
    return render(request, 'accounts/login.html', {'login_form': form})


def logout_view(request):
    logout(request)
    return redirect('login')