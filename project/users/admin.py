from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "is_staff", "is_active")
    search_fields = ("email", "full_name")
    readonly_fields = ("last_login",)
    fields = (
        "full_name",
        "email",
        "password",
        "is_active",
        "is_staff",
        "is_superuser",
        "last_login",
    )


admin.site.register(User, UserAdmin)
