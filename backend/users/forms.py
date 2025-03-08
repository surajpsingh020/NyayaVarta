from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

LANGUAGE_CHOICES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('bn', 'Bengali'),
    ('te', 'Telugu'),
    ('mr', 'Marathi'),
    ('ta', 'Tamil'),
    ('gu', 'Gujarati'),
    ('ur', 'Urdu'),
    ('kn', 'Kannada'),
    ('or', 'Odia'),
    ('ml', 'Malayalam'),
    ('pa', 'Punjabi'),
    ('as', 'Assamese'),
    ('mai', 'Maithili'),
    ('sd', 'Sindhi'),
    ('ks', 'Kashmiri'),
    ('kok', 'Konkani'),
    ('mni', 'Manipuri'),
    ('ne', 'Nepali'),
    ('sa', 'Sanskrit'),
    ('brx', 'Bodo'),
    ('sat', 'Santhali'),
]

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    language_preference = forms.ChoiceField(choices=LANGUAGE_CHOICES, required=True)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "language_preference")
        
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already taken")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this Email id is already registered")
        return email