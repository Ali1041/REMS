from django.urls import path,include
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name='account'
urlpatterns=[
    path('login',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('',home,name='home'),
    path('signup/<slug:slug>',SignUpView.as_view(),name='signup')
    # path('buyer/',include('buyer.url'))
]