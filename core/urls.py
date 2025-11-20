from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from core.views import submit_tutor_request
from core.views import request_tutor_success

urlpatterns = [

    path("", views.home, name="home"),

    path("dr-bianca/", views.dr_bianca, name="dr_bianca"),
    path("tormod/", views.tormod, name="tormod"),
    path("dr-amar/", views.dr_amar, name="dr_amar"),
    path("dr-don/", views.dr_don, name="dr_don"),
    path("dr-claire/", views.dr_claire, name="dr_claire"),
    path("dr-arjun/", views.dr_arjun, name="dr_arjun"),

    path("maths-tutors/", views.maths_tutors, name="maths_tutors"),

    path("subjects/", views.subjects, name="subjects"),
    path("university-tutors/", views.university_tutors, name="university_tutors"),
    path("university-tutors/biology/", views.biology_tutors, name="biology_tutors"),
    path("university-tutors/chemistry/", views.chemistry_tutors, name="chemistry_tutors"),
    path("university-tutors/computer-science/", views.computer_science_tutors, name="computer_science_tutors"),
    path("university-tutors/economics/", views.economics_tutors, name="economics_tutors"),
    path("university-tutors/engineering/", views.engineering_tutors, name="engineering_tutors"),
    path("university-tutors/finance/", views.finance_tutors, name="finance_tutors"),
    path("university-tutors/law/", views.law_tutors, name="law_tutors"),
    path("university-tutors/physics/", views.physics_tutors, name="physics_tutors"),
    path("university-tutors/politics/", views.politics_tutors, name="politics_tutors"),
    path("university-tutors/psychology/", views.psychology_tutors, name="psychology_tutors"),

    path("dissertation-tutors/", views.dissertation_tutors, name="dissertation_tutors"),
    path("dissertation-tutors/academic-writing/", views.academic_writing_tutors, name="academic_writing_tutors"),
    path("dissertation-tutors/english/", views.english_tutors, name="english_tutors"),
    path("dissertation-tutors/essay/", views.essay_tutors, name="essay_tutors"),
    path("dissertation-tutors/research-methods/", views.research_methods_tutors, name="research_methods_tutors"),
    path("dissertation-tutors/study-skills/", views.study_skills_tutors, name="study_skills_tutors"),
    path("dissertation-tutors/writing/", views.writing_tutors, name="writing_tutors"),
    path("dissertation-tutors/london/", views.london_dissertation_tutors, name="london_dissertation_tutors"),
    path("dissertation-tutors/cambridge/", views.cambridge_dissertation_tutors, name="cambridge_dissertation_tutors"),
    path("dissertation-tutors/oxford/", views.oxford_dissertation_tutors, name="oxford_dissertation_tutors"),
    path("dissertation-tutors/manchester/", views.manchester_dissertation_tutors, name="manchester_dissertation_tutors"),
    
    path("a-level-tutors/", views.a_level_tutors, name="a_level_tutors"),
    path("a-level-tutors/accounting/", views.a_level_accounting_tutors, name="a_level_accounting_tutors"),
    path("a-level-tutors/biology/", views.a_level_biology_tutors, name="a_level_biology_tutors"),
    path("a-level-tutors/chemistry/", views.a_level_chemistry_tutors, name="a_level_chemistry_tutors"),
    path("a-level-tutors/economics/", views.a_level_economics_tutors, name="a_level_economics_tutors"),
    path("a-level-tutors/english/", views.a_level_english_tutors, name="a_level_english_tutors"),
    path("a-level-tutors/further-maths/", views.a_level_further_maths_tutors, name="a_level_further_maths_tutors"),
    path("a-level-tutors/history/", views.a_level_history_tutors, name="a_level_history_tutors"),
    path("a-level-tutors/maths/", views.a_level_maths_tutors, name="a_level_maths_tutors"),
    path("a-level-tutors/physics/", views.a_level_physics_tutors, name="a_level_physics_tutors"),
    path("a-level-tutors/psychology/", views.a_level_psychology_tutors, name="a_level_psychology_tutors"),

    path("gcse-tutors/", views.gcse_tutors, name="gcse_tutors"),
    path("gcse-tutors/biology/", views.gcse_biology_tutors, name="gcse_biology_tutors"),
    path("gcse-tutors/chemistry/", views.gcse_chemistry_tutors, name="gcse_chemistry_tutors"),
    path("gcse-tutors/computer-science/", views.gcse_computer_science_tutors, name="gcse_computer_science_tutors"),
    path("gcse-tutors/english-language/", views.gcse_english_language_tutors, name="gcse_english_language_tutors"),
    path("gcse-tutors/geography/", views.gcse_geography_tutors, name="gcse_geography_tutors"),
    path("gcse-tutors/history/", views.gcse_history_tutors, name="gcse_history_tutors"),
    path("gcse-tutors/maths/", views.gcse_maths_tutors, name="gcse_maths_tutors"),
    path("gcse-tutors/physics/", views.gcse_physics_tutors, name="gcse_physics_tutors"),
    path("gcse-tutors/science/", views.gcse_science_tutors, name="gcse_science_tutors"),
    path("gcse-tutors/spanish/", views.gcse_spanish_tutors, name="gcse_spanish_tutors"),

    path("ib-tutors/", views.ib_tutors, name="ib_tutors"),
    path("ib-tutors/biology/", views.ib_biology_tutors, name="ib_biology_tutors"),
    path("ib-tutors/chemistry/", views.ib_chemistry_tutors, name="ib_chemistry_tutors"),
    path("ib-tutors/economics/", views.ib_economics_tutors, name="ib_economics_tutors"),
    path("ib-tutors/english-language/", views.ib_english_language_tutors, name="ib_english_language_tutors"),
    path("ib-tutors/maths/", views.ib_maths_tutors, name="ib_maths_tutors"),
    path("ib-tutors/physics/", views.ib_physics_tutors, name="ib_physics_tutors"),
    path("ib-tutors/london/", views.london_ib_tutors, name="london_ib_tutors"),
    path("ib-tutors/cambridge/", views.cambridge_ib_tutors, name="cambridge_ib_tutors"),
    path("ib-tutors/oxford/", views.oxford_ib_tutors, name="oxford_ib_tutors"),
    path("ib-tutors/manchester/", views.manchester_ib_tutors, name="manchester_ib_tutors"),

    path("online-tutors/", views.online_tutors, name="online_tutors"),
    path("online-tutors/aca/", views.aca_tutors, name="aca_tutors"),
    path("online-tutors/acca/", views.acca_tutors, name="acca_tutors"),
    path("online-tutors/accounting/", views.accounting_tutors, name="accounting_tutors"),
    path("online-tutors/architecture/", views.architecture_tutors, name="architecture_tutors"),
    path("online-tutors/econometrics/", views.econometrics_tutors, name="econometrics_tutors"),
    path("online-tutors/engineering/", views.online_engineering_tutors, name="online_engineering_tutors"),
    path("online-tutors/r/", views.r_tutors, name="r_tutors"),
    path("online-tutors/spss/", views.spss_tutors, name="spss_tutors"),
    path("online-tutors/stata/", views.stata_tutors, name="stata_tutors"),
    path("online-tutors/statistics/", views.statistics_tutors, name="statistics_tutors"),

    # University Admissions
    path("admissions-tutors/", views.admissions_tutors, name="admissions_tutors"),
    path("11-plus-tutors/", views.eleven_plus_tutors, name="11_plus_tutors"),
    path("common-entrance-tutors/", views.common_entrance_tutors, name="common_entrance_tutors"),
    path("admission-test-tutors/", views.admission_test_tutors, name="admission_test_tutors"),
    path("ucas-tutors/", views.ucas_tutors, name="ucas_tutors"),
    path("personal-statement-tutors/", views.personal_statement_tutors, name="personal_statement_tutors"),
    path("university-admission/", views.university_admission, name="university_admission"),
    path("cambridge-admission-tutors/", views.cambridge_admission_tutors, name="cambridge_admission_tutors"),
    path("edinburgh-admission-tutors/", views.edinburgh_admission_tutors, name="edinburgh_admission_tutors"),
    path("oxford-admission-tutors/", views.oxford_admission_tutors, name="oxford_admission_tutors"),
    path("ucl-admission-tutors/", views.ucl_admission_tutors, name="ucl_admission_tutors"),
    
    path("oxbridge-admissions/", views.oxbridge_admissions, name="oxbridge_admissions"),
    path("ahaa-tutors/", views.ahaa_tutors, name="ahaa_tutors"),
    path("bmat-tutors/", views.bmat_tutors, name="bmat_tutors"),
    path("cat-tutors/", views.cat_tutors, name="cat_tutors"),
    path("ctmua-tutors/", views.ctmua_tutors, name="ctmua_tutors"),
    path("elat-tutors/", views.elat_tutors, name="elat_tutors"),
    path("engaa-tutors/", views.engaa_tutors, name="engaa_tutors"),
    path("gat-tutors/", views.gat_tutors, name="gat_tutors"),
    path("hat-tutors/", views.hat_tutors, name="hat_tutors"),
    path("hspsaa-tutors/", views.hspsaa_tutors, name="hspsaa_tutors"),
    path("lnat-tutors/", views.lnat_tutors, name="lnat_tutors"),
    path("mat-tutors/", views.mat_tutors, name="mat_tutors"),
    path("mlat-tutors/", views.mlat_tutors, name="mlat_tutors"),
    path("pat-tutors/", views.pat_tutors, name="pat_tutors"),
    path("step-tutors/", views.step_tutors, name="step_tutors"),
    path("tsa-tutors/", views.tsa_tutors, name="tsa_tutors"),
    
    path("undergraduate-admissions/", views.undergraduate_admissions, name="undergraduate_admissions"),
    path("cambridge-admissions-tutors/", views.cambridge_admissions_tutors, name="cambridge_admissions_tutors"),
    path("durham-admissions-tutors/", views.durham_admissions_tutors, name="durham_admissions_tutors"),
    path("edinburgh-admissions-tutors/", views.edinburgh_admissions_tutors, name="edinburgh_admissions_tutors"),
    path("imperial-admissions-tutors/", views.imperial_admissions_tutors, name="imperial_admissions_tutors"),
    path("kings-college-admissions-tutors/", views.kings_college_admissions_tutors, name="kings_college_admissions_tutors"),
    path("lse-admissions-tutors/", views.lse_admissions_tutors, name="lse_admissions_tutors"),
    path("oxford-admissions-tutors/", views.oxford_admissions_tutors, name="oxford_admissions_tutors"),
    path("st-andrews-admissions-tutors/", views.st_andrews_admissions_tutors, name="st_andrews_admissions_tutors"),
    path("ucl-admissions-tutors/", views.ucl_admissions_tutors, name="ucl_admissions_tutors"),
    path("warwick-admissions-tutors/", views.warwick_admissions_tutors, name="warwick_admissions_tutors"),
    
    path("postgraduate-admissions/", views.postgraduate_admissions, name="postgraduate_admissions"),
    path("bcl-tutors/", views.bcl_tutors, name="bcl_tutors"),
    path("business-school-admissions-tutors/", views.business_school_admissions_tutors, name="business_school_admissions_tutors"),
    path("emba-tutors/", views.emba_tutors, name="emba_tutors"),
    path("gdl-tutors/", views.gdl_tutors, name="gdl_tutors"),
    path("gmat-tutors/", views.gmat_tutors, name="gmat_tutors"),
    path("law-school-admissions-tutors/", views.law_school_admissions_tutors, name="law_school_admissions_tutors"),
    path("masters-tutors/", views.masters_tutors, name="masters_tutors"),
    path("mba-admissions-tutors/", views.mba_admissions_tutors, name="mba_admissions_tutors"),
    
    path("medical-admissions/", views.medical_admissions, name="medical_admissions"),
    path("bmsat-tutors/", views.bmsat_tutors, name="bmsat_tutors"),
    path("gamsat-tutors/", views.gamsat_tutors, name="gamsat_tutors"),
    path("hpat-tutors/", views.hpat_tutors, name="hpat_tutors"),
    path("imat-tutors/", views.imat_tutors, name="imat_tutors"),
    path("mcat-tutors/", views.mcat_tutors, name="mcat_tutors"),
    path("ucat-tutors/", views.ucat_tutors, name="ucat_tutors"),
    
    path("us-admissions/", views.us_admissions, name="us_admissions"),
    path("act-tutors/", views.act_tutors, name="act_tutors"),
    path("ap-tutors/", views.ap_tutors, name="ap_tutors"),
    path("college-application-tutors/", views.college_application_tutors, name="college_application_tutors"),
    path("gre-tutors/", views.gre_tutors, name="gre_tutors"),
    path("isee-tutors/", views.isee_tutors, name="isee_tutors"),
    path("lsat-tutors/", views.lsat_tutors, name="lsat_tutors"),
    path("sat-tutors/", views.sat_tutors, name="sat_tutors"),
    path("ssat-tutors/", views.ssat_tutors, name="ssat_tutors"),

    # Resources
    path("resources/", views.resources, name="resources"),
    path("resources/ucl_economics/", TemplateView.as_view(template_name="core/Resources/ucl_economics.html"), name="ucl_economics"),
    path("resources/imperial_economics_finance/", TemplateView.as_view(template_name="core/Resources/imperial_economics_finance.html"), name="imperial_economics_finance"),
    path("resources/imperial_management/", TemplateView.as_view(template_name="core/Resources/imperial_management.html"), name="imperial_management"),
    path("resources/lbs_mba/", TemplateView.as_view(template_name="core/Resources/lbs_mba.html"), name="lbs_mba"),
    path("resources/cambridge/", TemplateView.as_view(template_name="core/Resources/cambridge.html"), name="cambridge"),
    path("resources/imperial_college_london/", TemplateView.as_view(template_name="core/Resources/imperial_college_london.html"), name="imperial_college_london"),
    path("resources/lse/", TemplateView.as_view(template_name="core/Resources/lse.html"), name="lse"),
    path("resources/ucl/", TemplateView.as_view(template_name="core/Resources/ucl.html"), name="ucl"),
    path('resources/ethics/', views.tutor_ethics, name='tutor_ethics'),
    path('resources/lesson-planning/', views.tutor_lesson_planning, name='tutor_lesson_planning'),
    path('resources/platform-guidelines/', views.tutor_platform, name='tutor_platform'),
    path('resources/assessment-standards/', views.tutor_assessment_standards, name='tutor_assessment_standards'),

    # Find Tutors
    path("find-tutors/", views.find_tutors, name="find_tutors"),
    path('find-tutors-results/', views.find_tutors_results, name='find_tutors_results'),

    # Pricing
    path("pricing/", views.pricing, name="pricing"),

    # Log In
    path("login/", views.login_view, name="login"),
    path('login/tuition/', views.tuition_login, name='tuition_login'),
    path('login/reset/', views.reset_tuition_password, name='reset_tuition_password'),
    
    path('login/consultancy/', views.consultancy_login, name='consultancy_login'),
    path('consultancy/reset-password/', views.consultancy_reset_password, name='consultancy_reset_password'),
    path('consultancy/login-help/', views.consultancy_login_help, name='consultancy_login_help'),
    path('consultancy/signup/', views.consultancy_signup, name='consultancy_signup'),

    path('consultancy/profile/', views.consultancy_profile, name='consultancy_profile'),
    path('consultancy/job-application/', views.consultancy_job_application, name='consultancy_job_application'),
    path('consultancy/application-success/', views.consultancy_application_success, name='consultancy_application_success'),


    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='core/Log In/password_reset_confirm.html'
         ), 
         name='password_reset_confirm'),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='core/Log In/password_reset_complete.html'
         ), 
         name='password_reset_complete'),

    # Become Tutor
    path("become-a-tutor/", views.become_a_tutor, name="become_a_tutor"),
    path("getting-started-as-a-tutor/", views.getting_started_as_a_tutor, name="getting_started_as_a_tutor"),
    path("how-to-tutor/", views.how_to_tutor, name="how_to_tutor"),
    path("how-to-tutor-online/", views.how_to_tutor_online, name="how_to_tutor_online"),

    # Request Tutor
    path("request-tutor/", views.request_tutor, name="request_tutor"),
    path("request/submit/", submit_tutor_request, name="submit_tutor_request"),
    path("request/success/", request_tutor_success, name="request_tutor_success"),

]