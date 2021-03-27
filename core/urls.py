from django.urls import path
from users import views as uesr_view

app_name = "core"

urlpatterns = [
    path("", uesr_view.HomeView.as_view(), name="home"),
]
