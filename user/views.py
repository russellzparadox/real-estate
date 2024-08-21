from django.contrib.auth import login
from django.contrib.auth.views import LoginView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import SignUpForm, CustomLoginForm


# Create your views here.
class SignUpView(FormView):
    template_name = "user/register.html"
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()  # Save the new user
        login(self.request, user)  # Log in the user after registration
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = CustomLoginForm
    # redirect_authenticated_user = True
    success_url = reverse_lazy('index')  # Redirect to home after successful login


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'user/forgot-password.html'
    email_template_name = 'password_reset_email.html'
    # subject_template_name = 'password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('index')
