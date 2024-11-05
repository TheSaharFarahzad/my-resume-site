from django.urls import path
from . import views

urlpatterns = [
    path("resume/", views.resume_view, name="resume"),
]
