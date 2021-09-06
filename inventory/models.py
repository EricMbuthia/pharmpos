from django.db import models
from django.urls.base import reverse
from django.utils import timezone
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
        return self.name

class Products(models.Model):
    item_name = models.CharField(max_length = 100)
    item_type = models.ForeignKey(ProductType , on_delete = models.CASCADE)
    brand_name = models.CharField(max_length = 100)
    chemical_name = models.CharField(max_length = 100)
<<<<<<< HEAD
    receiving_name =  models.CharField(max_length = 100,  null= True )
    receiving_number = models.IntegerField( null = True)
    dispensing_name = models.CharField(max_length = 100, null = True)
    dispensing_number = models.IntegerField(  null = True)
    date_time_entered = models.DateTimeField(default = timezone.now() )
    
=======
    date_time_entered = models.DateTimeField(default = timezone.now() )
>>>>>>> 8c8472c2c43ffa7227b85880fdc9f3c767386487

    def __str__(self):
        return self.item_name
    
class Stores(models.Model):
    storename = models.CharField(max_length =100)
    def __str__(self):
        return self.storename
    
##To be used in case of an internal order
##Drugs stored as in invoice
##Then multiplied later
# class MainStores(models.Model):
#     storename = models.CharField(max_length=100)

class Inventory(models.Model):
    product = models.ForeignKey(Products, on_delete = models.CASCADE)
    store = models.ForeignKey(Stores, models.CASCADE)
    quantity = models.IntegerField()
    def __str__(self):
        return self.product.item_name
    # def get_absolute_url(self):
    #     # return reverse("inventory:inventory_drug_list", kwargs = {"store_id":self.store.id})
    #     return reverse("inventory:inventory_detail", kwargs = {"pk":self.product.id})
    
    
    class Meta:
        unique_together = ('product', 'store')

class Suppliers(models.Model):
    #supp_id = models.IntegerField()
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name
    
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
###Look for template to capture data with the right grouping of drugs
    def __str__(self):
        return self.date_time_entry
<<<<<<< HEAD
class ReceivingTemplate(models.Model):
    receiving_unit_name =  models.CharField(max_length = 100)
    receiving_unit_number = models.IntegerField()
    dispensing_unit_name = models.CharField(max_length = 100)
    dispensing_unit_number = models.IntegerField()
    def __str__(self):
        return self.receiving_unit_name
=======
>>>>>>> 8c8472c2c43ffa7227b85880fdc9f3c767386487

class InventoryCard(models.Model):
    product_moving = models.ForeignKey(Products , on_delete = models.CASCADE)
    store_involved = models.ForeignKey(Stores, on_delete = models.CASCADE)
    quantity_balance = models.IntegerField()
    date_time_of_movement = models.DateTimeField( default =  timezone.now)
    user_involved = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "inventory_card_user_involved")
    #case_involved_id = models.IntegerField()## can be used to query a db record
    case_involved_description =models.CharField(max_length = 100) ## Can be used to find the actual db(sold/external_order/internal_order)
    
    def __str__(self):
        return self.product_moving


