from django.contrib import admin
from .models import User, SocialMedia, Experience, Skill, Language, Education


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "birthday",
        "job_title_main",
        "job_title_details",
    )
    search_fields = ("username", "first_name", "last_name", "email")
    list_filter = ("job_title_main", "job_title_details", "birthday")
    ordering = ("username",)


class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("user", "platform", "url", "icon")
    search_fields = ("user__username", "platform")
    list_filter = ("platform",)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "role", "formatted_dates", "company_address")
    search_fields = ("user__username", "company", "role")
    list_filter = ("company", "role")

    def formatted_dates(self, obj):
        return f"{obj.start_date.strftime('%b %Y')} - {'Present' if not obj.end_date else obj.end_date.strftime('%b %Y')}"

    formatted_dates.short_description = "Dates"


class SkillAdmin(admin.ModelAdmin):
    list_display = ("user", "skill_name", "years_of_experience")
    search_fields = ("user__username", "skill_name")
    list_filter = ("years_of_experience",)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ("user", "language_name", "proficiency_level")
    search_fields = ("user__username", "language_name")
    list_filter = ("proficiency_level",)


class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "university_name",
        "formatted_dates",
        "degree",
        "field_of_study",
        "university_address",
    )
    search_fields = ("user__username", "university_name", "field_of_study")
    list_filter = ("degree",)

    def formatted_dates(self, obj):
        return f"{obj.start_date.strftime('%b %Y')} - {'Present' if not obj.end_date else obj.end_date.strftime('%b %Y')}"

    formatted_dates.short_description = "Dates"


admin.site.register(User, UserAdmin)
admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Education, EducationAdmin)
