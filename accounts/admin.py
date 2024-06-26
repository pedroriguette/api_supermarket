from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ["id", "full_name", "username", "email", "is_active", "is_staff", "is_superuser", "created_at", "updated_at"]
    list_display_links = ["id", "full_name", "username", "email"]
    list_filter = ["is_active", "is_staff", "is_superuser", "created_at", "updated_at"]
    search_fields = ["full_name", "username", "email"]
    ordering = ["full_name", "username", "is_active", "is_superuser", "created_at", "updated_at"]
    actions = ["activate_users", "deactivate_users"]
    fieldsets = (
        ("Informações de Acesso", {
            "fields": (
                "username",
                "password"
            )
        }),
        ("Informações Pessoais", {
            "fields": (
                "full_name",
                "email",
                "is_trusty"
            )
        }),
        ("Permissões", {
            "fields": (
                "groups",
                "user_permissions",
                "is_active",
                "is_staff",
                "is_superuser",
            )
        })
    )

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Ativar Usuários"

    def deactivate_users(self, request, queryset):
        queryset. update(is_active=True)

    deactivate_users.short_description = "Desativar Usuários"


admin.site.register(User, CustomUserAdmin)
