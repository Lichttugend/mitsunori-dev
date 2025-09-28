from django.contrib import admin
from .models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}