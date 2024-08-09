from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Video, Student
from .forms import VideoForm, StudentRegistrationForm

def home(request):
    return render(request, 'academy/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('teacher_dashboard')
                else:
                    return redirect('student_dashboard')
        else:
            # If form is not valid, re-render the login page with errors
            return render(request, 'academy/login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'academy/login.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def teacher_dashboard(request):
    return render(request, 'academy/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'academy/student_dashboard.html')

def upload_video(request):
    if not request.user.is_superuser:
        return redirect('student_dashboard')NotImplementedError/

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_dashboard')
    else:
        form = VideoForm()

    return render(request, 'academy/upload_video.html', {'form': form})
def register_student(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        student_form = StudentRegistrationForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('student_dashboard')
    else:
        user_form = UserCreationForm()
        student_form = StudentRegistrationForm()

    return render(request, 'academy/register_student.html', {
        'user_form': user_form,
        'student_form': student_form
    })