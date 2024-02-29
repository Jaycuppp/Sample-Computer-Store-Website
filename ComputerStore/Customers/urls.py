from django.urls import path
from . import views

urlpatterns = [
    path('CreateUser', views.User_Register , name='CreateAccount'),
    path('UserLogin', views.Login_Auth, name='LoginPage'),
    path('UserLogout', views.User_Logout, name='LogoutPage'),
    path('UserForgotPassword', views.User_Forgot_Password , name='ForgotPassword'),
]