from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True,
                               widget=forms.EmailInput(attrs={'class':'sign__input', 'placeholder' : 'Email'}))
                               
    password = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class':'sign__input', 'placeholder' :'Password'}))




class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'sign__input', 'placeholder': 'Password'}),
        required=True
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'sign__input', 'placeholder': 'Repeat Password'}),
        required=True
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'sign__input', 'placeholder': 'Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'sign__input', 'placeholder': 'Phone Number'}),
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if not username.isalnum():
            raise forms.ValidationError('Username can only contain letters and numbers.')

        if len(username) < 5:
            raise forms.ValidationError('Username must be at least 5 characters.')

        if len(username) > 15:
            raise forms.ValidationError('Username must be at most 15 characters.')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken.')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use')
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('This phone number is already registered')
        return phone_number
    
    
    def clean_password_repeat(self):
        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password != password_repeat:
            raise forms.ValidationError('Passwords must match')
        return password_repeat


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password']) 
        if commit:
            user.save()
        return user



class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('profile_image', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'bio')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form__input', 'id': 'id_username'}),
            'first_name': forms.TextInput(attrs={'class': 'form__input', 'id': 'id_first_name'}),
            'last_name': forms.TextInput(attrs={'class': 'form__input', 'id': 'id_last_name'}),
            'email': forms.EmailInput(attrs={'class': 'form__input', 'id': 'id_email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form__input', 'id': 'id_phone_number'}),
            'bio': forms.Textarea(attrs={'class': 'form__textarea', 'id': 'id_bio', 'rows': 4}),
            'profile_image': forms.FileInput(attrs={'class': 'file-upload__input', 'id': 'id_profile_image'}),
        }

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if phone and User.objects.exclude(id=self.instance.id).filter(phone_number=phone).exists():
            raise forms.ValidationError('Phone number already exists')
        return phone


    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError('Username already exists')
        else:
            return username
