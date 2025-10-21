from django.contrib import admin
from .models import ProfilePic,Project,Contact

@admin.register(ProfilePic)
class ProfilePicAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']  # You can add more fields if needed
admin.site.register(Project)


@admin.register(Contact)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'created_at')
    search_fields = ('full_name', 'email', 'message')