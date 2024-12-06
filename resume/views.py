from django.shortcuts import render
from .models import User, SocialMedia, Experience, Skill, Education, Language
from collections import defaultdict


def resume_view(request):
    user = User.objects.first()  # Retrieve the first user
    social_media_links = SocialMedia.objects.filter(user=user)
    experiences = Experience.objects.filter(user=user)
    skills = Skill.objects.filter(user=user)
    education = Education.objects.filter(user=user)
    languages = Language.objects.filter(user=user)

    # Group skills by years of experience
    grouped_skills = defaultdict(list)
    for skill in skills:
        grouped_skills[skill.years_of_experience].append(skill.skill_name)

    # Sort the skills by years of experience in descending order
    sorted_grouped_skills = dict(
        sorted(grouped_skills.items(), key=lambda item: item[0], reverse=True)
    )

    context = {
        "user": user,
        "social_media_links": social_media_links,
        "experiences": experiences,
        "grouped_skills": sorted_grouped_skills,  # Pass the sorted grouped skills dictionary
        "education": education,
        "languages": languages,
        "job_title_main": user.job_title_main,
        "job_title_details": user.job_title_details,
        "profile_picture_url": user.profile_picture.url,
    }

    return render(request, "resume/resume.html", context)
