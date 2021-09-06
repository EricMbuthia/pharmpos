from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(ProductType)
admin.site.register(Products)
admin.site.register(Stores)
admin.site.register(Inventory)
admin.site.register(Suppliers)
admin.site.register(ExternalOrder)
admin.site.register(InventoryCard)

class ReceivingTemplateAdmin(admin.ModelAdmin):
    list_display = ("receiving_unit_name","receiving_unit_number","dispensing_unit_name","dispensing_unit_number")
    fieldsets = (
        ("Receiving Detail", {
            "fields":("receiving_unit_name","receiving_unit_number"),
            "description": "Add receiving detail Here"
        }),
        ("Dispensing Detail", {
            "fields":("dispensing_unit_name","dispensing_unit_number"),
            "description": "Add dispensing detail here"
        })
    )
admin.site.register(ReceivingTemplate, ReceivingTemplateAdmin)