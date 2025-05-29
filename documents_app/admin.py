from django.contrib import admin
from .models import Document, Invoice

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "residence", "date_creation", "summary")
    list_filter = ("category", "residence", "date_creation")
    search_fields = ("title", "summary", "residence__residence_name")
    readonly_fields = ("date_creation",)
    ordering = ("-date_creation",)

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    exclude = ("residence", "category")  # as you said
    list_display = ("id", "title", "charge", "residence", "date_creation")
    list_filter = ("residence",)
    search_fields = ("title", "charge__title", "residence__residence_name")
    readonly_fields = ("residence", "category", "date_creation")
    ordering = ("-date_creation",)
