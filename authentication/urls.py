
from django.urls import path,include
#from .views import login_view, register_user, password_reset_request
from .views import password_reset_request
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', allauth.account.views.LoginView, name="login"),
    path('logout/', allauth.account.views.LogoutView, name="logout"),
    path('signup/',allauth.account.views.SignupView, name="signup"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("password_reset/", password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),   
   
    ]
