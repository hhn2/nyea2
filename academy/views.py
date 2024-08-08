from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Video, Student
from .forms import VideoForm, UserForm, StudentForm

def home(request):
    return render(request, 'academy/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user_type == 'teacher':
                return redirect('teacher_dashboard')
            elif user_type == 'student':
                return redirect('student_dashboard')
        else:
            return render(request, 'academy/login.html', {'error': 'Invalid credentials'})
    return render(request, 'academy/login.html')

@login_required
def teacher_dashboard(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request, 'academy/teacher_dashboard.html')

@login_required
def student_dashboard(request):
    if request.user.is_superuser:
        return redirect('home')
    student = Student.objects.get(user=request.user)
    videos = Video.objects.filter(level=student.level)
    return render(request, 'academy/student_dashboard.html', {'videos': videos})

@login_required
def upload_video(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_dashboard')
    else:
        form = VideoForm()
    return render(request, 'academy/upload_video.html', {'form': form})

@login_required
def register_student(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)  # Set the password properly
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            return redirect('teacher_dashboard')
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'academy/register_student.html', {'user_form': user_form, 'student_form': student_form})
