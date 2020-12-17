from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import PasswordResetConfirmView,\
    PasswordResetCompleteView,PasswordResetView,PasswordResetDoneView
app_name='account'

# all url patterns for this app mostly contains the login,signup,reset,forget urls
urlpatterns=[
    path('login',LoginHelpView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',home,name='home'),
    path('signup/<slug:slug>',SignUpView.as_view(),name='signup'),
    path('reset_password/',PasswordResetView.as_view(),name='reset_password'),
    path('password_reset_done/',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete')
]