from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
class RegistrationForm(forms.Form):
    user_name  = forms.CharField(label = 'Username', max_length=30)
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(
        label = 'Password',
        widget = forms.PasswordInput()
    )
    password2 = forms.CharField(
        label = 'Password confirm',
        widget = forms.PasswordInput()
    )

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Password do not match!')
    
    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if not re.search(r'^\w+$', user_name):
            raise forms.ValidationError('Username can only contain alphanumberic characters and the underscore!')
        try:
            User.objects.get(username=user_name)
        except ObjectDoesNotExist:
            return user_name
        raise forms.ValidationError('Username is already taken!')