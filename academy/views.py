from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .models import Video, Student
from .forms import VideoForm, UserForm, StudentRegistrationForm, StudentForm

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
        form = AuthenticationForm()
    return render(request, 'academy/login.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def teacher_dashboard(request):
    if request.method == 'POST':
        if 'create_student' in request.POST:
            student_form = StudentRegistrationForm(request.POST)
            if student_form.is_valid():
                student_form.save()
                return redirect('teacher_dashboard')
        elif 'upload_video' in request.POST:
            video_form = VideoForm(request.POST, request.FILES)
            if video_form.is_valid():
                video_form.save()
                return redirect('teacher_dashboard')
    else:
        student_form = StudentRegistrationForm()
        video_form = VideoForm()
    return render(request, 'academy/teacher_dashboard.html', {
        'student_form': student_form,
        'video_form': video_form,
    })
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


@login_required
def videos_by_level(request, level):
    student = Student.objects.get(user=request.user)
    if student.level == level:
        videos = Video.objects.filter(level=level)
        return render(request, 'academy/videos_by_level.html', {'videos': videos})
    else:
        return redirect('student_dashboard')  # Redirect to student's dashboard if levels don't match