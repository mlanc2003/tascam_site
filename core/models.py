from django.db import models
from django.contrib.auth.models import User

class TutorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=200, blank=True)
    highest_degree = models.CharField(max_length=200, blank=True)
    university = models.CharField(max_length=200, blank=True)
    subjects = models.CharField(max_length=300, blank=True)
    profile_picture = models.ImageField(upload_to="tutor_profiles/", blank=True, null=True)

    def __str__(self):
        return self.full_name


class TutorApplication(models.Model):
    profile = models.ForeignKey(TutorProfile, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="tutor_resumes/")
    cover_letter = models.TextField()
    availability = models.CharField(max_length=200)
    rates = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application - {self.profile.full_name}"
