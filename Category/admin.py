from django.contrib import admin
from Category.models import Category_model

@admin.register(Category_model)
class Category_admin(admin.ModelAdmin):
    list_display = ('image', 'title')
    list_display_links = ('image', 'title')