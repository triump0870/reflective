from authtools.admin import NamedUserAdmin
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from reflective.employees.admin import EmployeeStackedAdmin
from reflective.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(NamedUserAdmin):
    inlines = [EmployeeStackedAdmin]

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    list_display_links = ('username', 'name',)
    search_fields = ["name"]
