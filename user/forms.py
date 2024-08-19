# forms.py

from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm


class CustomLoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                     'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
            'placeholder': 'Email Address'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                     'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
            'placeholder': 'Password'
        })
    )


class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                     'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
            'placeholder': 'Create a Password'
        })
    )

    class Meta:
        model = get_user_model()  # Use the custom User model
        fields = ['email', 'first_name', 'last_name', 'phone_number', 'username', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                         'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
                'placeholder': 'Email Address'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                         'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                         'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
                'placeholder': 'Last Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                         'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
                'placeholder': 'User Name'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control g-color-black g-bg-white g-bg-white--focus g-brd-gray-light-v3 '
                         'g-brd-primary--hover rounded-0 g-py-13 g-px-15',
                'placeholder': 'Phone Number'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user
