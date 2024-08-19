from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views

from user.views import SignUpView, CustomLoginView, ResetPasswordView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup_view"),
    # path('signup/success/', TemplateView.as_view(template_name='base.html'), name='signup-success'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
         name='password_reset_complete'),

]
