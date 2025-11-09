from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class UserLogin(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:home')
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid email or password")
        return render(request, 'account/login.html', {'form': form})

    

class UserRegister(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = (
                authenticate(request, username=username, password=password)
                or authenticate(request, email=email, password=password)
            )

            if user is not None:
                login(request, user)
                return redirect('/')

        return render(request, 'account/register.html', {'form': form})


class UserLogout(View):
    def get(self, request):
        logout(request)
        return redirect('home:home') 
    
    
@method_decorator(login_required, name='dispatch')
class UserProfile(View):
    template_name = 'account/profile.html'

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
        return render(request, self.template_name, {'form': form})
    
        