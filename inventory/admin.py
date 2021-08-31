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