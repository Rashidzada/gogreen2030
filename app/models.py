from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('developer', 'Developer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    company = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    user_role = models.CharField(max_length=20, choices=USER_ROLES, default='student')

    def __str__(self):
        return f"{self.user.username}'s profile - {self.get_user_role_display()}"

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='education')
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.degree} at {self.institution}"

class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.username} - {self.name}"

class SocialLink(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_links')
    platform = models.CharField(max_length=50)  # e.g., 'LinkedIn', 'GitHub', 'Twitter'
    url = models.URLField()

    def __str__(self):
        return f"{self.user.username} - {self.platform}"