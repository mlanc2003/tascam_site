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

    authorized = models.CharField(max_length=50, blank=True)
    convicted = models.CharField(max_length=50, blank=True)
    conviction_explanation = models.TextField(blank=True)
    desired_salary = models.CharField(max_length=100, blank=True)
    teaching_mode = models.CharField(max_length=50, blank=True)
    notice_period = models.CharField(max_length=100, blank=True)
    additional_comments = models.TextField(blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application - {self.profile.full_name}"

class TutorRequest(models.Model):
    subject = models.CharField(max_length=255)
    hours_needed = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    details = models.TextField(blank=True)

    address_standard = models.CharField(max_length=255, blank=True)
    lat_standard = models.FloatField(null=True, blank=True)
    lng_standard = models.FloatField(null=True, blank=True)

    address_uni = models.CharField(max_length=255, blank=True)
    lat_uni = models.FloatField(null=True, blank=True)
    lng_uni = models.FloatField(null=True, blank=True)

    subject_standard_other = models.CharField(max_length=255, blank=True)
    subject_uni_other = models.CharField(max_length=255, blank=True)

    university = models.CharField(max_length=255, blank=True)
    university_other = models.CharField(max_length=255, blank=True)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tutor Request from {self.first_name} {self.last_name}"