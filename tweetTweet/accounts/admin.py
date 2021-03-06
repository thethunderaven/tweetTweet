from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ProfileChangeForm,  ProfileCreationForm
from .models import Profile

# Register your models here.
class ProfileAdmin(UserAdmin):
    add_form = ProfileCreationForm
    form = ProfileChangeForm
    model = Profile
    list_display = ['email', 'username']

admin.site.register(Profile, ProfileAdmin)