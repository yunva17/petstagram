from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from . import forms


class LoginView(View):
    def get(self, request):
        pass

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")


def log_out(request):
    logout(request)
    return redirect("/")
