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
                self.add_error(
                    "password", forms.ValidationError("PASSWORD IS WRONG"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("USER DOESNT EXIST"))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ['email', 'name', 'username', 'password']

        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        name = self.cleaned_data.get("name")
        password = self.cleaned_data.get("password")

        user = models.User.objects.create_user(username,
                                               email,
                                               name,
                                               password)

        user.save()
