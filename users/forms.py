import phonenumbers
from django import forms
from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("비밀번호 틀림"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("아이디 존재 안함"))


class SignUpForm(forms.Form):
    pass
