from django import forms
from django.contrib import admin
from .models import Property


from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        "id", 
        "property_number", 
        "property_type", 
        "residence", 
        "owner", 
        "property_size", 
        "number_of_rooms", 
        "status", 
        "created_at"
    )
    list_filter = ("property_type", "residence", "status", "created_at")
    search_fields = (
        "property_number", 
        "owner__email", 
        "owner__username", 
        "residence__residence_name"
    )
    autocomplete_fields = ("owner", "residence")
    ordering = ("-created_at",)
