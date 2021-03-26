from django.urls import path
from . import views
app_name = "users"

urlpatterns = [

    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login", views.LogInView.as_view(), name="login"),
]
