from django.contrib import admin
from .models import Monster, Magic, Trap


@admin.register(Monster, Magic, Trap)
class ViewAdmin(admin.ModelAdmin):
    pass