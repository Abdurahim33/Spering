from django.contrib import admin
from About.models import About_model, About_spering


@admin.register(About_model)
class Aboutadmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title')
    list_display_links = ('image', 'title', 'sub_title')



@admin.register(About_spering)
class Aboutsperingadmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'sub_title')
    list_display_links = ('image', 'title', 'sub_title')
