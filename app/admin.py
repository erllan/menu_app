from django.contrib import admin
from .models import Menu, Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ["name",]


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    fields = ["name", "parent", "category"]
