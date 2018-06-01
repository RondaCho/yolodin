from django.contrib import admin
from din.models import Din


@admin.register(Din)
class DinAdmin(admin.ModelAdmin):
    pass