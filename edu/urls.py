from django.urls import path

# getting all functions we coded in views to create url for it
from edu.views import *

# adding application name
app_name = "edu"

# urlspatterns
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    # path('about/',AboutView.as_view(),name='about'),
    path('student-register/',StudentRegisterView.as_view(),name='register'),
    path('student-login/',StudentLoginView.as_view(),name='login'),
    path('student-logout/',StudentLogoutView.as_view(),name='logout'),
    path('student-profile/',StudentProfileView.as_view(),name='profile'),
    path('student-update-profile/<int:id>',UpdateProfileView.as_view(),name='update_profile'),
    path('forget-password/',ForgotPasswordView.as_view(),name='forget_password'),
    path('reset-password/<email>/<token>/',ResetPasswordView.as_view(),name='reset_password'),
]