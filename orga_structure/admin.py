from django.contrib import admin
from .models import Orga_Structure

# Register your models here.

class OragAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "parentId")

admin.site.register(Orga_Structure)

