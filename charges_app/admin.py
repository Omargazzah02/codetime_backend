from django.contrib import admin
from .models import Charge , PropertyCharge , ChargePrediction

# Register your models here.

@admin.register(Charge)
class ChargeAdmin(admin.ModelAdmin):
    list_display = ('id', 'residence', 'title', 'category', 'date_creation', 'price')
    list_filter = (
        'residence',          # filter by residence
        'category',           # filter by category
        'date_creation',      # filter by creation date (will show by day, month, year)
    )
    search_fields = ('title',)  # optional: add a search box on titles
    ordering = ('-date_creation',)  # optional: newest first



@admin.register(PropertyCharge)
class PropertyChargeAdmin(admin.ModelAdmin):
    list_display = ("charge", "property", "part")
    list_filter = ("charge", "property__residence")
    search_fields = ("charge__title", "property__property_number", "property__property_type")
    autocomplete_fields = ("charge", "property")  # Helpful if many entries


@admin.register(ChargePrediction)
class ChargePredictionAdmin(admin.ModelAdmin):
    list_display = ('residence', 'category', 'year', 'month', 'predicted_price')
