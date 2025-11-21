from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



#==================== USER LOGIN ====================
class UserLoginView(View):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['email'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('/')
            else:
                form.add_error(None, "Invalid email or password")
                messages.error(request, 'username or password is wrong', 'warning')
        return render(request, 'account/login.html', {'form': form})

    
#==================== USER REGISTER ====================
class UserRegisterView(View):
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    
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
                messages.success(request, 'you registered in successfully', 'success')
                return redirect('/')
        return render(request, 'account/register.html', {'form': form})


#==================== USER LOGOUT ====================
class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully')
        return redirect('home:home') 
  
    
#==================== USER PROFILE ====================   
class UserProfileView(LoginRequiredMixin, View):
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
    
        