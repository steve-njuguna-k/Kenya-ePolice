from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm

class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'Old Password',}))
    new_password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'New Password',}))
    new_password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control mb-4','type': 'password','name': 'password1','placeholder': 'Confirm Password',}))

    class Meta:
        model = User
        fields = ('old_password','new_password1','new_password2',)

def clean_old_password(self):
    old_password = self.cleaned_data["old_password"]
    if not self.user.check_password(old_password):
        raise forms.ValidationError(
            self.error_messages['password_incorrect'],
            code='password_incorrect',
        )
    return old_password