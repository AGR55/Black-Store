from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'auth.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
                return render(request, 'auth.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('Home')


def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username', None)
            password = form.cleaned_data.get('password', None)
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.error(request, 'Invalid')
        else:
            messages.error(request, 'Invalid')

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
