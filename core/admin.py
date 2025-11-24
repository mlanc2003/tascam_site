from django.contrib import admin
from .models import TutorProfile, TutorApplication, TutorRequest

# Register your models here.
admin.site.register(TutorProfile)
admin.site.register(TutorApplication)
admin.site.register(TutorRequest)