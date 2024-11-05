from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class SocialMedia(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_media"
    )
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.platform} ({self.url})"


class Experience(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_experiences"
    )
    company = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    still_working = models.BooleanField(default=False)
    role = models.CharField(max_length=100)
    task_description = models.TextField()
    skills_used = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company}"


class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="skills")
    skill_name = models.CharField(max_length=100)
    years_of_experience = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.skill_name} ({self.years_of_experience} years)"


class Language(models.Model):
    PROFICIENCY_CHOICES = [
        ("native", "Native"),
        ("fluent", "Fluent"),
        ("intermediate", "Intermediate"),
        ("basic", "Basic"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="languages")
    language_name = models.CharField(max_length=100)
    proficiency_level = models.CharField(
        max_length=50,
        choices=PROFICIENCY_CHOICES,
    )

    def __str__(self):
        return f"{self.language_name} - {self.proficiency_level}"


class Education(models.Model):
    DEGREE_CHOICES = [
        ("bachelor", "Bachelor's Degree"),
        ("master", "Master's Degree"),
        ("phd", "PhD"),
        ("associate", "Associate's Degree"),
        ("diploma", "Diploma"),
        ("certificate", "Certificate"),
        ("other", "Other"),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="education")
    university_name = models.CharField(max_length=100)
    university_address = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=100)
    degree = models.CharField(max_length=50, choices=DEGREE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    still_studying = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.university_name}"
