from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .models import TutorProfile, TutorApplication, TutorRequest

def home(request):
    subjects = [
        {"name": "GCSE Tutors", "url": reverse("gcse_tutors")},
        {"name": "ACA Tutors", "url": reverse("aca_tutors")},
        {"name": "Econometrics Tutors", "url": reverse("econometrics_tutors")},
        {"name": "ACCA Tutors", "url": reverse("acca_tutors")},
        {"name": "Economics Tutors", "url": reverse("economics_tutors")},
        {"name": "Politics Tutors", "url": reverse("politics_tutors")},
        {"name": "A-level Tutors", "url": reverse("a_level_tutors")},
        {"name": "Acad. Writing Tutors", "url": reverse("academic_writing_tutors")},
        {"name": "Engineering Tutors", "url": reverse("engineering_tutors")},
        {"name": "Psychology Tutors", "url": reverse("psychology_tutors")},
        {"name": "IB Tutors", "url": reverse("ib_tutors")},
        {"name": "Accounting Tutors", "url": reverse("accounting_tutors")},
        {"name": "English Literature Tutors", "url": reverse("english_tutors")},
        {"name": "Architecture Tutors", "url": reverse("architecture_tutors")},
        {"name": "Essay Tutors", "url": reverse("essay_tutors")},
        {"name": "SAT Tutors", "url": reverse("sat_tutors")},
        {"name": "Finance Tutors", "url": reverse("finance_tutors")},
        {"name": "SPSS Tutors", "url": reverse("spss_tutors")},
        {"name": "University Admission Tutors", "url": reverse("university_admission")},
        {"name": "STEP Mathematics Tutors", "url": reverse("step_tutors")},
    ]

    tutors = [
        {
            "id": 1,
            "name": "Dr. Bianca",
            "image": "/static/images/tutor-sample.jpg",
            "rating": "5.0",
            "university": "UCL",
            "subjects": ["Health", "Science"],
            "bio": "Experienced UCL lecturer and PhD in Health Sciences."
        },
        {
            "id": 2,
            "name": "Prof. Adam",
            "image": "/static/images/tutor-sample.jpg",
            "rating": "4.9",
            "university": "Oxford",
            "subjects": ["Economics", "Finance"],
            "bio": "Oxford-trained economist with 10+ years tutoring experience."
        },
    ]

    return render(request, "core/home.html", {
        "subjects": subjects,
        "tutors": tutors
    })

def dr_bianca(request):
    return render(request, "core/dr_bianca.html")
def tormod(request):
    return render(request, "core/tormod.html")
def dr_amar(request):
    return render(request, "core/dr_amar.html")
def dr_don(request):
    return render(request, "core/dr_don.html")
def dr_claire(request):
    return render(request, "core/dr_claire.html")
def dr_arjun(request):
    return render(request, "core/dr_arjun.html")

def maths_tutors(request):
    return render(request, "core/maths_tutors.html")

def subjects(request):
    return render(request, "core/Tutoring/subjects.html")

COMMON_CONTEXT = {
    "button_text": "Request Tutor"
}

# ----------------------------
# UNIVERSITY SUBJECT TUTOR PAGES
# ----------------------------

def university_tutors(request):
    return render(request, "core/Tutoring/university_tutors.html", COMMON_CONTEXT)

def biology_tutors(request):
    return render(request, "core/Tutoring/biology_tutors.html", COMMON_CONTEXT)

def chemistry_tutors(request):
    return render(request, "core/Tutoring/chemistry_tutors.html", COMMON_CONTEXT)

def computer_science_tutors(request):
    return render(request, "core/Tutoring/computer_science_tutors.html", COMMON_CONTEXT)

def economics_tutors(request):
    return render(request, "core/Tutoring/economics_tutors.html", COMMON_CONTEXT)

def engineering_tutors(request):
    return render(request, "core/Tutoring/engineering_tutors.html", COMMON_CONTEXT)

def finance_tutors(request):
    return render(request, "core/Tutoring/finance_tutors.html", COMMON_CONTEXT)

def law_tutors(request):
    return render(request, "core/Tutoring/law_tutors.html", COMMON_CONTEXT)

def physics_tutors(request):
    return render(request, "core/Tutoring/physics_tutors.html", COMMON_CONTEXT)

def politics_tutors(request):
    return render(request, "core/Tutoring/politics_tutors.html", COMMON_CONTEXT)

def psychology_tutors(request):
    return render(request, "core/Tutoring/psychology_tutors.html", COMMON_CONTEXT)

def dissertation_tutors(request):
    return render(request, "core/Tutoring/dissertation_tutors.html", COMMON_CONTEXT)

def academic_writing_tutors(request):
    return render(request, "core/Tutoring/academic_writing_tutors.html", COMMON_CONTEXT)

def english_tutors(request):
    return render(request, "core/Tutoring/english_tutors.html", COMMON_CONTEXT)

def essay_tutors(request):
    return render(request, "core/Tutoring/essay_tutors.html", COMMON_CONTEXT)

def research_methods_tutors(request):
    return render(request, "core/Tutoring/research_methods_tutors.html", COMMON_CONTEXT)

def study_skills_tutors(request):
    return render(request, "core/Tutoring/study_skills_tutors.html", COMMON_CONTEXT)

def writing_tutors(request):
    return render(request, "core/Tutoring/writing_tutors.html", COMMON_CONTEXT)

def london_dissertation_tutors(request):
    return render(request, "core/Tutoring/london_dissertation_tutors.html", COMMON_CONTEXT)

def cambridge_dissertation_tutors(request):
    return render(request, "core/Tutoring/cambridge_dissertation_tutors.html", COMMON_CONTEXT)

def oxford_dissertation_tutors(request):
    return render(request, "core/Tutoring/oxford_dissertation_tutors.html", COMMON_CONTEXT)

def manchester_dissertation_tutors(request):
    return render(request, "core/Tutoring/manchester_dissertation_tutors.html", COMMON_CONTEXT)


# ----------------------------
# A-LEVEL TUTORS
# ----------------------------

def a_level_tutors(request):
    return render(request, "core/Tutoring/a_level_tutors.html", COMMON_CONTEXT)

def a_level_accounting_tutors(request):
    return render(request, "core/Tutoring/a_level_accounting_tutors.html", COMMON_CONTEXT)

def a_level_biology_tutors(request):
    return render(request, "core/Tutoring/a_level_biology_tutors.html", COMMON_CONTEXT)

def a_level_chemistry_tutors(request):
    return render(request, "core/Tutoring/a_level_chemistry_tutors.html", COMMON_CONTEXT)

def a_level_economics_tutors(request):
    return render(request, "core/Tutoring/a_level_economics_tutors.html", COMMON_CONTEXT)

def a_level_english_tutors(request):
    return render(request, "core/Tutoring/a_level_english_tutors.html", COMMON_CONTEXT)

def a_level_further_maths_tutors(request):
    return render(request, "core/Tutoring/a_level_further_maths_tutors.html", COMMON_CONTEXT)

def a_level_history_tutors(request):
    return render(request, "core/Tutoring/a_level_history_tutors.html", COMMON_CONTEXT)

def a_level_maths_tutors(request):
    return render(request, "core/Tutoring/a_level_maths_tutors.html", COMMON_CONTEXT)

def a_level_physics_tutors(request):
    return render(request, "core/Tutoring/a_level_physics_tutors.html", COMMON_CONTEXT)

def a_level_psychology_tutors(request):
    return render(request, "core/Tutoring/a_level_psychology_tutors.html", COMMON_CONTEXT)


# ----------------------------
# GCSE TUTORS
# ----------------------------

def gcse_tutors(request):
    return render(request, "core/Tutoring/gcse_tutors.html", COMMON_CONTEXT)

def gcse_biology_tutors(request):
    return render(request, "core/Tutoring/gcse_biology_tutors.html", COMMON_CONTEXT)

def gcse_chemistry_tutors(request):
    return render(request, "core/Tutoring/gcse_chemistry_tutors.html", COMMON_CONTEXT)

def gcse_computer_science_tutors(request):
    return render(request, "core/Tutoring/gcse_computer_science_tutors.html", COMMON_CONTEXT)

def gcse_english_language_tutors(request):
    return render(request, "core/Tutoring/gcse_english_language_tutors.html", COMMON_CONTEXT)

def gcse_geography_tutors(request):
    return render(request, "core/Tutoring/gcse_geography_tutors.html", COMMON_CONTEXT)

def gcse_history_tutors(request):
    return render(request, "core/Tutoring/gcse_history_tutors.html", COMMON_CONTEXT)

def gcse_maths_tutors(request):
    return render(request, "core/Tutoring/gcse_maths_tutors.html", COMMON_CONTEXT)

def gcse_physics_tutors(request):
    return render(request, "core/Tutoring/gcse_physics_tutors.html", COMMON_CONTEXT)

def gcse_science_tutors(request):
    return render(request, "core/Tutoring/gcse_science_tutors.html", COMMON_CONTEXT)

def gcse_spanish_tutors(request):
    return render(request, "core/Tutoring/gcse_spanish_tutors.html", COMMON_CONTEXT)


# ----------------------------
# IB TUTORS
# ----------------------------

def ib_tutors(request):
    return render(request, "core/Tutoring/ib_tutors.html", COMMON_CONTEXT)

def ib_biology_tutors(request):
    return render(request, "core/Tutoring/ib_biology_tutors.html", COMMON_CONTEXT)

def ib_chemistry_tutors(request):
    return render(request, "core/Tutoring/ib_chemistry_tutors.html", COMMON_CONTEXT)

def ib_economics_tutors(request):
    return render(request, "core/Tutoring/ib_economics_tutors.html", COMMON_CONTEXT)

def ib_english_language_tutors(request):
    return render(request, "core/Tutoring/ib_english_language_tutors.html", COMMON_CONTEXT)

def ib_maths_tutors(request):
    return render(request, "core/Tutoring/ib_maths_tutors.html", COMMON_CONTEXT)

def ib_physics_tutors(request):
    return render(request, "core/Tutoring/ib_physics_tutors.html", COMMON_CONTEXT)

def london_ib_tutors(request):
    return render(request, "core/Tutoring/london_ib_tutors.html", COMMON_CONTEXT)

def cambridge_ib_tutors(request):
    return render(request, "core/Tutoring/cambridge_ib_tutors.html", COMMON_CONTEXT)

def oxford_ib_tutors(request):
    return render(request, "core/Tutoring/oxford_ib_tutors.html", COMMON_CONTEXT)

def manchester_ib_tutors(request):
    return render(request, "core/Tutoring/manchester_ib_tutors.html", COMMON_CONTEXT)


# ----------------------------
# ONLINE + SPECIALITY SUBJECTS
# ----------------------------

def online_tutors(request):
    return render(request, "core/Tutoring/online_tutors.html", COMMON_CONTEXT)

def aca_tutors(request):
    return render(request, "core/Tutoring/aca_tutors.html", COMMON_CONTEXT)

def acca_tutors(request):
    return render(request, "core/Tutoring/acca_tutors.html", COMMON_CONTEXT)

def accounting_tutors(request):
    return render(request, "core/Tutoring/accounting_tutors.html", COMMON_CONTEXT)

def architecture_tutors(request):
    return render(request, "core/Tutoring/architecture_tutors.html", COMMON_CONTEXT)

def econometrics_tutors(request):
    return render(request, "core/Tutoring/econometrics_tutors.html", COMMON_CONTEXT)

def online_engineering_tutors(request):
    return render(request, "core/Tutoring/online_engineering_tutors.html", COMMON_CONTEXT)

def r_tutors(request):
    return render(request, "core/Tutoring/r_tutors.html", COMMON_CONTEXT)

def spss_tutors(request):
    return render(request, "core/Tutoring/spss_tutors.html", COMMON_CONTEXT)

def stata_tutors(request):
    return render(request, "core/Tutoring/stata_tutors.html", COMMON_CONTEXT)

def statistics_tutors(request):
    return render(request, "core/Tutoring/statistics_tutors.html", COMMON_CONTEXT)


# ----------------------------
# UNIVERSITY ADMISSIONS
# ----------------------------

def admissions_tutors(request): 
    return render(request, "core/University Admissions/admissions_tutors.html", COMMON_CONTEXT)

def eleven_plus_tutors(request): 
    return render(request, "core/University Admissions/11_plus_tutors.html", COMMON_CONTEXT)

def common_entrance_tutors(request): 
    return render(request, "core/University Admissions/common_entrance_tutors.html", COMMON_CONTEXT)

def admission_test_tutors(request):
    return render(request, "core/University Admissions/admission_test_tutors.html", COMMON_CONTEXT)

def ucas_tutors(request): 
    return render(request, "core/University Admissions/ucas_tutors.html", COMMON_CONTEXT)

def personal_statement_tutors(request): 
    return render(request, "core/University Admissions/personal_statement_tutors.html", COMMON_CONTEXT)

def university_admission(request): 
    return render(request, "core/University Admissions/university_admission.html", COMMON_CONTEXT)

def cambridge_admission_tutors(request):
    return render(request, "core/University Admissions/cambridge_admission_tutors.html", COMMON_CONTEXT)

def edinburgh_admission_tutors(request): 
    return render(request, "core/University Admissions/edinburgh_admission_tutors.html", COMMON_CONTEXT)

def oxford_admission_tutors(request): 
    return render(request, "core/University Admissions/oxford_admission_tutors.html", COMMON_CONTEXT)

def ucl_admission_tutors(request): 
    return render(request, "core/University Admissions/ucl_admission_tutors.html", COMMON_CONTEXT)

def oxbridge_admissions(request): 
    return render(request, "core/University Admissions/oxbridge_admissions.html", COMMON_CONTEXT)

def ahaa_tutors(request): 
    return render(request, "core/University Admissions/ahaa_tutors.html", COMMON_CONTEXT)

def bmat_tutors(request):
    return render(request, "core/University Admissions/bmat_tutors.html", COMMON_CONTEXT)

def cat_tutors(request):
    return render(request, "core/University Admissions/cat_tutors.html", COMMON_CONTEXT)

def ctmua_tutors(request):
    return render(request, "core/University Admissions/ctmua_tutors.html", COMMON_CONTEXT)

def elat_tutors(request): 
    return render(request, "core/University Admissions/elat_tutors.html", COMMON_CONTEXT)

def engaa_tutors(request): 
    return render(request, "core/University Admissions/engaa_tutors.html", COMMON_CONTEXT)

def gat_tutors(request):
    return render(request, "core/University Admissions/gat_tutors.html", COMMON_CONTEXT)

def hat_tutors(request):
    return render(request, "core/University Admissions/hat_tutors.html", COMMON_CONTEXT)

def hspsaa_tutors(request): 
    return render(request, "core/University Admissions/hspsaa_tutors.html", COMMON_CONTEXT)

def lnat_tutors(request): 
    return render(request, "core/University Admissions/lnat_tutors.html", COMMON_CONTEXT)

def mat_tutors(request): 
    return render(request, "core/University Admissions/mat_tutors.html", COMMON_CONTEXT)

def mlat_tutors(request):
    return render(request, "core/University Admissions/mlat_tutors.html", COMMON_CONTEXT)

def pat_tutors(request):
    return render(request, "core/University Admissions/pat_tutors.html", COMMON_CONTEXT)

def step_tutors(request): 
    return render(request, "core/University Admissions/step_tutors.html", COMMON_CONTEXT)

def tsa_tutors(request): 
    return render(request, "core/University Admissions/tsa_tutors.html", COMMON_CONTEXT)


# ----------------------------
# UNDERGRADUATE ADMISSIONS
# ----------------------------

def undergraduate_admissions(request):
    return render(request, "core/University Admissions/undergraduate_admissions.html", COMMON_CONTEXT)

def cambridge_admissions_tutors(request): 
    return render(request, "core/University Admissions/cambridge_admissions_tutors.html", COMMON_CONTEXT)

def durham_admissions_tutors(request): 
    return render(request, "core/University Admissions/durham_admissions_tutors.html", COMMON_CONTEXT)

def edinburgh_admissions_tutors(request): 
    return render(request, "core/University Admissions/edinburgh_admissions_tutors.html", COMMON_CONTEXT)

def imperial_admissions_tutors(request):
    return render(request, "core/University Admissions/imperial_admissions_tutors.html", COMMON_CONTEXT)

def kings_college_admissions_tutors(request):
    return render(request, "core/University Admissions/kings_college_admissions_tutors.html", COMMON_CONTEXT)

def lse_admissions_tutors(request):
    return render(request, "core/University Admissions/lse_admissions_tutors.html", COMMON_CONTEXT)

def oxford_admissions_tutors(request):
    return render(request, "core/University Admissions/oxford_admissions_tutors.html", COMMON_CONTEXT)

def st_andrews_admissions_tutors(request):
    return render(request, "core/University Admissions/st_andrews_admissions_tutors.html", COMMON_CONTEXT)

def ucl_admissions_tutors(request):
    return render(request, "core/University Admissions/ucl_admissions_tutors.html", COMMON_CONTEXT)

def warwick_admissions_tutors(request):
    return render(request, "core/University Admissions/warwick_admissions_tutors.html", COMMON_CONTEXT)


# ----------------------------
# POSTGRADUATE ADMISSIONS
# ----------------------------

def postgraduate_admissions(request):
    return render(request, "core/University Admissions/postgraduate_admissions.html", COMMON_CONTEXT)

def bcl_tutors(request):
    return render(request, "core/University Admissions/bcl_tutors.html", COMMON_CONTEXT)

def business_school_admissions_tutors(request):
    return render(request, "core/University Admissions/business_school_admissions_tutors.html", COMMON_CONTEXT)

def emba_tutors(request):
    return render(request, "core/University Admissions/emba_tutors.html", COMMON_CONTEXT)

def gdl_tutors(request):
    return render(request, "core/University Admissions/gdl_tutors.html", COMMON_CONTEXT)

def gmat_tutors(request):
    return render(request, "core/University Admissions/gmat_tutors.html", COMMON_CONTEXT)

def law_school_admissions_tutors(request):
    return render(request, "core/University Admissions/law_school_admissions_tutors.html", COMMON_CONTEXT)

def masters_tutors(request):
    return render(request, "core/University Admissions/masters_tutors.html", COMMON_CONTEXT)

def mba_admissions_tutors(request):
    return render(request, "core/University Admissions/mba_admissions_tutors.html", COMMON_CONTEXT)


# ----------------------------
# MEDICAL ADMISSIONS
# ----------------------------

def medical_admissions(request):
    return render(request, "core/University Admissions/medical_admissions.html", COMMON_CONTEXT)

def bmsat_tutors(request):
    return render(request, "core/University Admissions/bmsat_tutors.html", COMMON_CONTEXT)

def gamsat_tutors(request):
    return render(request, "core/University Admissions/gamsat_tutors.html", COMMON_CONTEXT)

def hpat_tutors(request):
    return render(request, "core/University Admissions/hpat_tutors.html", COMMON_CONTEXT)

def imat_tutors(request):
    return render(request, "core/University Admissions/imat_tutors.html", COMMON_CONTEXT)

def mcat_tutors(request):
    return render(request, "core/University Admissions/mcat_tutors.html", COMMON_CONTEXT)

def ucat_tutors(request):
    return render(request, "core/University Admissions/ucat_tutors.html", COMMON_CONTEXT)


# ----------------------------
# US ADMISSIONS
# ----------------------------

def us_admissions(request):
    return render(request, "core/University Admissions/us_admissions.html", COMMON_CONTEXT)

def act_tutors(request):
    return render(request, "core/University Admissions/act_tutors.html", COMMON_CONTEXT)

def ap_tutors(request):
    return render(request, "core/University Admissions/ap_tutors.html", COMMON_CONTEXT)

def college_application_tutors(request):
    return render(request, "core/University Admissions/college_application_tutors.html", COMMON_CONTEXT)

def gre_tutors(request):
    return render(request, "core/University Admissions/gre_tutors.html", COMMON_CONTEXT)

def isee_tutors(request):
    return render(request, "core/University Admissions/isee_tutors.html", COMMON_CONTEXT)

def lsat_tutors(request):
    return render(request, "core/University Admissions/lsat_tutors.html", COMMON_CONTEXT)

def sat_tutors(request):
    return render(request, "core/University Admissions/sat_tutors.html", COMMON_CONTEXT)

def ssat_tutors(request):
    return render(request, "core/University Admissions/ssat_tutors.html", COMMON_CONTEXT)

# Resources
def resources(request):
    return render(request, "core/Resources/resources.html")
def tutor_resources(request):
    return render(request, 'core/Resources/tutor_resources.html')

def client_resources(request):
    return render(request, 'core/Resources/client_resources.html')
def client_parent_guide(request):
    return render(request, 'core/Resources/client_parent_guide.html')

def client_student_success(request):
    return render(request, 'core/Resources/client_student_success.html')

def client_working_with_tutors(request):
    return render(request, 'core/Resources/client_working_with_tutors.html')

def blogs(request):
    return render(request, 'core/Resources/blogs.html')

def cambridge(request):
    return render(request, 'core/Resources/cambridge.html')
def imperial_college_london(request):
    return render(request, 'core/Resources/imperial_college_london.html')
def imperial_economics(request):
    return render(request, 'core/Resources/imperial_economics.html')
def imperial_management(request):
    return render(request, 'core/Resources/imperial_management.html')
def lbs_mba(request):
    return render(request, 'core/Resources/lbs_mba.html')
def lse(request):
    return render(request, 'core/Resources/lse.html')
def ucl(request):
    return render(request, 'core/Resources/ucl.html')
def ucl_economics(request):
    return render(request, 'core/Resources/ucl_economics.html')

def tutor_ethics(request):
    return render(request,"core/Resources/tutor_ethics.html")

def tutor_lesson_planning(request):
    return render(request, "core/Resources/tutor_lesson_planning.html")

def tutor_platform(request):
    return render(request, "core/Resources/tutor_platform.html")

def tutor_assessment_standards(request):
    return render(request, "core/Resources/tutor_assessment_standards.html")

# Find Tutors
def find_tutors(request):
    return render(request, "core/Find Tutors/find_tutors.html")

def find_tutors_results(request):
    level = request.GET.get("level", "")
    subject = request.GET.get("subject", "")

    # In the future, filter tutors dynamically based on these
    context = {"level": level, "subject": subject}

    # Return only the results HTML (no full page)
    return render(request, "core/Find Tutors/tutor_results_partial.html", context)

# Pricing
def pricing(request):
    return render(request, "core/Pricing/pricing.html")

# Log_In
def login_view(request):
    return render(request, "core/Log_In/login.html")
def tuition_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Redirecting to homepage...")
            return render(request, 'core/Log_In/tuition_login.html', {'redirect_home': True})
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'core/Log_In/tuition_login.html')

from django.contrib.auth.models import User
from django.core.mail import send_mail
def reset_tuition_password(request):
    if request.method == 'POST':
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')

        if email1 != email2:
            messages.error(request, "Emails do not match.")
            return render(request, 'core/Log_In/reset_tuition_password.html')

        # Check if email exists
        try:
            user = User.objects.get(email=email1)
        except User.DoesNotExist:
            messages.error(request, "No account found with that email.")
            return render(request, 'core/Log_In/reset_tuition_password.html')

        # Send password reset email using Django’s built-in functionality
        from django.contrib.auth.tokens import default_token_generator
        from django.utils.http import urlsafe_base64_encode
        from django.utils.encoding import force_bytes

        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        reset_link = f"http://127.0.0.1:8000/reset/{uid}/{token}/"

        send_mail(
            "TASCAM Password Reset",
            f"Click the link to reset your password:\n\n{reset_link}",
            "tascam.noreply@gmail.com",
            [email1],
            fail_silently=False,
        )

        messages.success(request, "A password reset link has been sent to your email address.")
    
    return render(request, 'core/Log_In/reset_tuition_password.html')

from django.shortcuts import render, redirect
from django.contrib import messages

def consultancy_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful! Redirecting to homepage...")
            return render(request, 'core/Log_In/consultancy_login.html', {'redirect_home': True})
        else:
            messages.error(request, "Invalid email or password. Please try again.")

    return render(request, 'core/Log_In/consultancy_login.html')

def consultancy_reset_password(request):
    if request.method == 'POST':
        email1 = request.POST.get('email1')
        email2 = request.POST.get('email2')
        if email1 == email2:
            messages.success(request, "A password reset link has been sent to your email.")
        else:
            messages.error(request, "Emails do not match. Please try again.")
    return render(request, 'core/Log_In/consultancy_reset_password.html')
def consultancy_login_help(request):
    return render(request, 'core/Log_In/consultancy_login_help.html')

def consultancy_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')

        # Validate email uniqueness
        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'core/Log_In/consultancy_signup.html')

        # Split name into first + last
        parts = name.split(" ", 1)
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ""

        # Create the user
        user = User.objects.create_user(
            username=email,       # username = email
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        # Optional: Log them in immediately
        login(request, user)

        TutorProfile.objects.create(
            user=user,
            full_name=name
        )

        messages.success(request, f"Welcome {first_name}! Your account has been created successfully.")
        return redirect('consultancy_profile')

    return render(request, 'core/Log_In/consultancy_signup.html')

def consultancy_profile(request):
    profile = TutorProfile.objects.get(user=request.user)

    if request.method == "POST":
        profile.bio = request.POST.get("bio")
        profile.phone = request.POST.get("phone")
        profile.location = request.POST.get("location")
        profile.highest_degree = request.POST.get("highest_degree")
        profile.university = request.POST.get("university")
        profile.subjects = request.POST.get("subjects")

        if "profile_picture" in request.FILES:
            profile.profile_picture = request.FILES["profile_picture"]

        profile.save()
        return redirect("consultancy_job_application")

    return render(request, "core/Log_In/profile.html", {"profile": profile})

def consultancy_job_application(request):
    profile = TutorProfile.objects.get(user=request.user)

    if request.method == "POST":
        TutorApplication.objects.create(
            profile=profile,
            resume=request.FILES.get("resume"),
            cover_letter=request.POST.get("cover_letter"),
            availability=request.POST.get("availability"),
            rates=request.POST.get("rates"),
            experience_years=request.POST.get("experience_years"),

            authorized=request.POST.get("authorized", ""),
            convicted=request.POST.get("convicted", ""),
            conviction_explanation=request.POST.get("conviction_explanation", ""),
            desired_salary=request.POST.get("desired_salary", ""),
            teaching_mode=request.POST.get("teaching_mode", ""),
            notice_period=request.POST.get("notice_period", ""),
            additional_comments=request.POST.get("additional_comments", ""),
        )

        return redirect("consultancy_application_success")

    return render(request, 'core/Log_In/job_application.html', {"profile": profile})

def consultancy_application_success(request):
    return render(request, "core/Log_In/application_success.html")

# Become Tutor
def become_a_tutor(request):
    return render(request, "core/Become Tutor/become_a_tutor.html")
def getting_started_as_a_tutor(request):
    return render(request, "core/Become Tutor/getting_started_as_a_tutor.html")

def how_to_tutor(request):
    return render(request, "core/Become Tutor/how_to_tutor.html")

def how_to_tutor_online(request):
    return render(request, "core/Become Tutor/how_to_tutor_online.html")

# Request Tutor
def request_tutor(request):
    return render(request, "core/Request Tutor/request_tutor.html")

from django.core.mail import send_mail

def submit_tutor_request(request):
    if request.method == "POST":

        print("DEBUG: View reached")

        subject = request.POST.get("subject", "")
        hours = request.POST.get("hours_needed", "")
        first = request.POST.get("first_name", "")
        last = request.POST.get("last_name", "")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        details = request.POST.get("details", "")

        address_standard = request.POST.get("address_standard", "")
        lat_standard = request.POST.get("lat_standard") or None
        lng_standard = request.POST.get("lng_standard") or None

        address_uni = request.POST.get("address_uni", "")
        lat_uni = request.POST.get("lat_uni") or None
        lng_uni = request.POST.get("lng_uni") or None

        subject_standard_other = request.POST.get("subject_standard_other", "")
        subject_uni_other = request.POST.get("subject_uni_other", "")

        university = request.POST.get("university", "")
        university_other = request.POST.get("university_other", "")

        TutorRequest.objects.create(
            subject=subject,
            hours_needed=hours,
            first_name=first,
            last_name=last,
            phone=phone,
            email=email,
            details=details,

            address_standard=address_standard,
            lat_standard=lat_standard,
            lng_standard=lng_standard,
            address_uni=address_uni,
            lat_uni=lat_uni,
            lng_uni=lng_uni,
            subject_standard_other=subject_standard_other,
            subject_uni_other=subject_uni_other,
            university=university,
            university_other=university_other,
        )

        message_body = f"""
        New Tutor Request Submitted:

        Name: {first} {last}
        Email: {email}
        Phone: {phone}

        Subject/Course: {subject}
        Tutoring Needed: {hours}

        Details:
        {details}
        """

        send_mail(
            subject="New Tutor Request - TASCAM Co Ltd",
            message=message_body,
            from_email="tascam.noreply@gmail.com",
            recipient_list=["tascam.noreply@gmail.com"],
            fail_silently=False,
        )

        messages.success(request, "Your request has been sent! We will contact you shortly.")
        return redirect("request_tutor_success")

    return redirect("request_tutor")

def request_tutor_success(request):
    return render(request, "core/Log_In/request_tutor_success.html")

def generate_button_text(filename):
    # Remove extension
    base = filename.replace(".html", "")

    # Remove "_tutors"
    base = base.replace("_tutors", "")

    # Replace underscores with spaces
    base = base.replace("_", " ")

    # Capitalize words
    subject_name = base.title()

    return f"Find My {subject_name} Tutor"

def subject_page(request, template_name):
    button_text = generate_button_text(template_name)

    return render(request, f"core/Tutoring/{template_name}", {
        "button_text": button_text
    })

def testimonials(request):
    return render(request, 'core/testimonials.html')