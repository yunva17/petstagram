from django.views import View
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from . import forms


class HomeView(View):
    def get(self, request):
        return render(request, "base.html")


class SignUpView(View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(request, "users/signup.html", {"form": form})

    def post(self, request):
        form = forms.SignUpForm()
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            name = form.cleaned_data.get("name")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return render(request, "users/signup.html", {"form": form})


class LogInView(View):

    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm()
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect("/")
