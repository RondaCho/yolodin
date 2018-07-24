from django.contrib import admin
from din.models import Din, Log


@admin.register(Din)
class DinAdmin(admin.ModelAdmin):
    pass

@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    pass