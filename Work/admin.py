from django.contrib import admin
from Work.models import Work_model

@admin.register(Work_model)
class Work_admin(admin.ModelAdmin):
    list_display = ('image', 'cost', 'title')
    list_display_links = ('image', 'cost', 'title')