# forms.py

from django import forms
from django.contrib.auth.models import User
from .models import Student, Video

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['level']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'level']
