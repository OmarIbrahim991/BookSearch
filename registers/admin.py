from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomCreationForm, CustomChangeForm
from .models import User

# Register your models here.
class CustomAdmin(UserAdmin):
    add_form = CustomCreationForm
    form = CustomChangeForm
    model = User
    list_display = ["id", "username", "password", "email",]#[field.name for field in User._meta.get_fields()]

admin.site.register(User, CustomAdmin)