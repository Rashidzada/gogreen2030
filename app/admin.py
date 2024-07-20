# admin.py

from django.contrib import admin
from .models import UserProfile, Education, Skill, SocialLink

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_role', 'location', 'company')
    search_fields = ('user__username', 'bio', 'location', 'company')
    list_filter = ('user_role',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('user', 'degree', 'institution', 'start_date', 'end_date')
    search_fields = ('user__username', 'institution', 'degree', 'field_of_study')
    list_filter = ('institution', 'degree')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    search_fields = ('user__username', 'name')

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'platform', 'url')
    search_fields = ('user__username', 'platform', 'url')

# Optional: Customize the admin site header and title
admin.site.site_header = "User Management Admin"
admin.site.site_title = "User Management Admin Portal"
admin.site.index_title = "Welcome to the User Management Admin"