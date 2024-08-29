from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('upload_video/', views.upload_video, name='upload_video'),
    path('videos/<str:level>/', views.videos_by_level, name='videos_by_level'),
    path('register_student/', views.register_student, name='register_student'),
    path('logout/', auth_views.LogoutView.as_view(next_page=''), name='logout'),  # This line should now work
    
]
