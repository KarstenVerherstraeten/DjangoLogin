from django.urls import path

from . import views

app_name = "login"
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add-task/", views.add_task, name="addTask"),
]