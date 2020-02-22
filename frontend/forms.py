from django.contrib.auth.models import User
from django import forms
class UserRegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Hasło',widget=forms.PasswordInput)
    password2=forms.CharField(label='Powtórz Hasło',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields = ('username','first_name','email')
        help_texts = {
            'username': None,
            
        }

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']   