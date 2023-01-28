from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'gender', 'password']
        widgets = {
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'gender': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }