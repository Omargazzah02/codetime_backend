from django import forms
from django.contrib import admin
from .models import Residence


from django.contrib import admin
from .models import Residence

@admin.register(Residence)
class ResidenceAdmin(admin.ModelAdmin):
    list_display = (
        "residence_name", 
        "city", 
        "zip_code", 
        "country", 
        "floor_count", 
        "has_parking", 
        "created_at", 
        "updated_at"
    )
    list_filter = ("city", "country", "has_parking")
    search_fields = ("residence_name", "city", "zip_code")
    ordering = ("-created_at",)
