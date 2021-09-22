from django import forms 
from django.conf import settings
# from django.core import validators 
from django.core.exceptions import ValidationError
from django.forms.formsets import formset_factory
from django.forms.widgets import NumberInput, Select, TextInput
from .models import ProductType, Stores, Products, Suppliers
def validate_item_id(item_id):
    print("Validate ITEM ID")
    print(item_id)
    if item_id == "0":
        print("Fineeeeeee")
    else:
        print("Nototototo")
    return item_id
##Drug Category Forms
drug_category_choices = [(drug_cat.id, drug_cat.name ) for drug_cat in ProductType.objects.all()]
# print(drug_category_choices)
store_choices = [(store.id, store.storename ) for store in Stores.objects.all()]
supplier_choices = [(supplier.id, supplier.name) for supplier in Suppliers.objects.all()]
drug_choices = [(drug_rec.id, drug_rec.chemical_name) for drug_rec in Products.objects.all()]
class DrugCategoryRegForm(forms.Form):
    drug_category_name = forms.CharField(widget = forms.TextInput(attrs= {'class': 'form-control'}),
     label = "Category" )
    drug_category_description = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control', 'rows':'4', 'cols': '50'}), 
    label = "Description")
    item_cat_id = forms.IntegerField( validators = [validate_item_id], required = False,)



##Drugs/ Products Forms
class ProductsForm(forms.Form):
    item_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = "Commonly Known")
    # item_type = forms.ModelMultipleChoiceField(widget = forms.Select(),queryset = ProductType.objects.all())
    item_type = forms.ChoiceField(choices= drug_category_choices)
    brand_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = "Brand Name")
    chemical_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'} ), label = "Chemical Name")
    receiving_name = forms.CharField(widget =  forms.TextInput(attrs={"class": "form-control"}), label ="Recieving Form")
    receiving_number = forms.CharField(widget = forms.TextInput(attrs={'class': "form-control"}), label = "Receing Quantity")
    dispensing_name = forms.CharField(widget = forms.TextInput(attrs= {"class":"form-control"}), label = "Dispencing Form")
    dispensing_number = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), label= "Dipensing Qauntity")
    # item_id = forms.CharField(widget = TextInput(attrs = {"value": "0"}), validators = [validate_item_id])
class ProductsFormUpdate(forms.Form):
    item_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = "Commonly Known")
    # item_type = forms.ModelMultipleChoiceField(widget = forms.Select(),queryset = ProductType.objects.all())
    item_type = forms.ChoiceField(choices= drug_category_choices)
    brand_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}), label = "Brand Name")
    chemical_name = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'} ), label = "Chemical Name")
    item_id = forms.IntegerField( validators = [validate_item_id], required = False,)
    receiving_name = forms.CharField(widget =  forms.TextInput(attrs={"class": "form-control"}), label ="Recieving Form")
    receiving_number = forms.CharField(widget = forms.TextInput(attrs={'class': "form-control"}), label = "Receing Quantity")
    dispensing_name = forms.CharField(widget = forms.TextInput(attrs= {"class":"form-control"}), label = "Dispencing Form")
    dispensing_number = forms.CharField(widget = forms.TextInput(attrs={"class":"form-control"}), label= "Dipensing Qauntity")


#### Stores Forms##############
class StoreRegForm(forms.Form):
    storename = forms.CharField(widget = forms.TextInput(attrs= {'class': 'form-control'}),label = "Store Name" )
    store_id = forms.IntegerField( validators = [validate_item_id], required = False,)


#####INVENTORY FORMS ###########
##Inventory Registration
class InventoryRegForm(forms.Form):
    product = forms.ChoiceField(widget =forms.Select(attrs = {"class": "form-control"}),choices =  drug_choices)
    store = forms.ChoiceField(widget= forms.Select(attrs={"class": "form-control"}),choices = store_choices, label ="Store")
    quantity =  forms.IntegerField(widget = NumberInput(attrs = {'class': 'form-control'}), label = "Quantinty in Store")
    store_id = forms.IntegerField( validators = [validate_item_id], required = False,)

##Assign Store Form
class AssignStoreForm(forms.Form):
    store = forms.ChoiceField(widget= forms.Select(attrs= {"class": "form-class"}),choices = [], label = "Stores Absent")
    quantity =  forms.IntegerField( label = "Quantinty in Store")
    product_id = forms.IntegerField( validators = [validate_item_id], required = False,)
    def __init__(self, absent_stores,product_id, *args, **kwargs):
        super(AssignStoreForm, self).__init__(*args, **kwargs)
        self.fields['store'].choices = absent_stores
        self.fields['product_id'].widget.attrs['value'] = product_id
            # self.absent_stores_list = absent_stores
    
##Update Quantity Form
class UpdateQauntityForm(forms.Form):
    product_id = forms.IntegerField( validators = [validate_item_id], required = False,)
    store_id = forms.IntegerField( validators = [validate_item_id], required = False,)
    quantity = forms.IntegerField( widget = forms.NumberInput(attrs = {"class":'form-class'}), label = "Quantity")


#### Supplier Forms##############
class SupplierRegForm(forms.Form):
    supplier_name = forms.CharField(widget = forms.TextInput(attrs= {'class': 'form-control', "id":"sup_nam"}),label = "Supplier Name" )
    supplier_email = forms.EmailField(widget = forms.EmailInput(attrs= {'class': 'form-control'}),label = "Email Address" )
    supplier_phone = forms.IntegerField(widget = forms.NumberInput(attrs = {"class":'form-class'}), label = "Phone Number" )
    supplier_id = forms.IntegerField( validators = [validate_item_id], required = False,)

class CreateExternalOrderForm(forms.Form):
    invoice_number = forms.CharField(widget = TextInput(attrs = {"class": "form-control"}), label = "Invoice Number")
    supplier = forms.ChoiceField(widget = forms.Select(attrs={"class": 'form-class'}), choices= supplier_choices, label= "Supplier")
    destination_store = forms.ChoiceField(widget= forms.Select(attrs = {"class":'form-class'}), choices = store_choices,  label = "Destination Store")
class DrugIntakeForm(forms.Form):
    item_name = forms.CharField(widget = forms.TextInput(attrs = {"class": "form-control", "id":"item_name"}),disabled = False,label = "Common Name")
    brand_name = forms.CharField(widget = forms.TextInput(attrs= {"class": "form-control", "id":"brand_name"}), disabled =False,label = "Brand Name")
    chemical_name =  forms.CharField(widget = forms.TextInput(attrs = {"class":"form-control", "id":"chemical_name"}),disabled = False, label = "Chemical Name")
    receiving_name = forms.CharField(widget= forms.TextInput(attrs= {"class":"form-control", "id":"receiving_name"}), disabled = False, label = "Receiving Form")
    receiving_number =  forms.CharField(widget = forms.TextInput(attrs= {"class":"form-control", "id":"receiving_number"}),disabled = False,label = "Receiving Quantity")
    dispensing_name = forms.CharField(widget = forms.TextInput(attrs ={"class":"form-control", "id":"dispensing_name"}), disabled = False, label = "Dispencing Form")
    dispensing_number = forms.CharField(widget= forms.TextInput(attrs= {"class":"form-control", "id":"dispensing_number"}), disabled = False,label = "Dispensing Number")
    drug_id = forms.IntegerField(widget = forms.NumberInput(attrs ={"style": "display: None;", "id":"drug_id"}) ,required= False)
    quantity =  forms.IntegerField(widget = forms.NumberInput(attrs= {"class":"form-control", "id":"quantity"}), label = "Quantity Ordered")
    price =  forms.FloatField(widget = forms.NumberInput(attrs= {"class":"form-control", "id":"price"}), label = "Price Per Each")
    total_price =  forms.FloatField(widget = forms.NumberInput(attrs= {"class":"form-control", "id":"total_price", "style": "display: None;",}), disabled=True ,label = "Total Price")
    # edit_check = forms.ChoiceField(widget = forms.CheckboxInput(attrs = {"class":"form-control"}), label = "Edit Check" )
