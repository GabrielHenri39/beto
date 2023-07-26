from django.contrib import admin
from .models import Users
from django.contrib.auth import admin as admin_auth
from .forms import UserChangeForm, UserCreationForm
# Register your models here.
@admin.register(Users)
class UsersAdmin(admin_auth.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = Users
