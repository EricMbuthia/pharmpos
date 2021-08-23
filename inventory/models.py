from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# from registration.models import Registration
from django.contrib.auth.models import User
# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length = 100)
    #type_id = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        self.name

class Products(models.Model):
    item_name = models.CharField(max_length = 100)
    item_type = models.ForeignKey(ProductType , on_delete = models.CASCADE)
    brand_name = models.CharField(max_length = 100)
    chemical_name = models.CharField(max_length = 100)
    date_time_entered = models.DateTimeField()

    def __str__(self):
        self.item_name
class Stores(models.Model):
    storename = models.CharField(max_length =100)
    #store_id = models.IntegerField()

    def __str__(self):
        self.storename

class Inventory(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    store = models.ForeignKey(Stores, models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        self.product

class Suppliers(models.Model):
    #supp_id = models.IntegerField()
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        self.name
    
class ExternalOrder(models.Model):
    #order_id = models.IntegerField()
    invoice_number = models.CharField(max_length = 100)
    supplier = models.ForeignKey(Suppliers, on_delete = models.CASCADE)
    destination_store = models.ForeignKey(Stores, on_delete = models.CASCADE)
    total_invoiced_amount = models.FloatField()
    date_time_entry = models.DateTimeField()
    user_involved = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "external_order_user_involved")
    approval = models.BooleanField(default = False)
    approver = models.ForeignKey(User, on_delete = models.CASCADE , related_name = "external_order_approver")
    products = models.JSONField(null = True)### more research on how to use foreignkeys

    def __str__(self):
        self.date_time_entry

class InventoryCard(models.Model):
    product_moving = models.ForeignKey(Products , on_delete = models.CASCADE)
    store_involved = models.ForeignKey(Stores, on_delete = models.CASCADE)
    quantity_balance = models.IntegerField()
    date_time_of_movement = models.DateTimeField( default =  timezone.now)
    user_involved = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "inventory_card_user_involved")
    #case_involved_id = models.IntegerField()## can be used to query a db record
    case_involved_description =models.CharField(max_length = 100) ## Can be used to find the actual db(sold/external_order/internal_order)
    
    def __str__(self):
        self.product_moving


