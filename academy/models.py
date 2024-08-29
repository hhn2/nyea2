# models.py

from django.db import models
from django.contrib.auth.models import User

class Level(models.Model):
    LEVEL_CHOICES = [
        ('levelone', 'Level One'),
        ('leveltwo', 'Level Two'),
        ('levelthree', 'Level Three'),
    ]
    name = models.CharField(max_length=100, choices=LEVEL_CHOICES, unique=True)

    def __str__(self):
        return self.get_name_display()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
