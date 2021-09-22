from django.forms.formsets import formset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, request
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils import timezone
import pandas as pd 
import sys
from .forms import *
from .models import *


# Create your views here.
###DRUG CATEGORY
def drug_category_reg(request):
    if request.method == "GET":
        drugCategoryRegForm = DrugCategoryRegForm()
        return render (request, "drug_category_reg.html", {'drugCategoryRegForm': drugCategoryRegForm})

    elif request.method == "POST" and request.is_ajax:
        drugCategoryRegForm = DrugCategoryRegForm(data = request.POST)
        if drugCategoryRegForm.is_valid():
            drug_category_name = request.POST.get("drug_category_name", False)
            drug_category_description = request.POST.get("drug_category_description", False)
            drug_cat_reg_data = ProductType(name = drug_category_name,  description = drug_category_description)
            drug_cat_reg_data.save()
            response_data = {'recieved': True, 'status': "ok"}
            return JsonResponse(response_data)
        else:
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)
    else:
        drugCategoryRegForm = DrugCategoryRegForm()
        return render (request, "drug_category_reg.html", {'drugCategoryRegForm': drugCategoryRegForm})
## List Categories available
def display_drug_categories(request):
    
    try:
        drug_cat_recs = ProductType.objects.all()
        print("happened")
        print(drug_cat_recs)
        return render(request, 'drug_category_lists.html',{'drug_cat_recs': drug_cat_recs})
    except:
        print(Exception)
        print("Errors", sys.exc_info()[0])
        return render(request, 'drug_category_lists.html',{'drug_cat_recs_error': "Could not Fetch"})
## Update Category
def drug_category_detail(request, pk):
    try:
        drug_cat_rec = ProductType.objects.get(id = pk)

        name = drug_cat_rec.name
        description = drug_cat_rec.description
        item_cat_id = drug_cat_rec.id
        
        drug_cat_rec_dict = {'drug_category_name':name, "drug_category_description":description, "item_cat_id":item_cat_id}
        print(drug_cat_rec_dict)
        drug_cat_form = DrugCategoryRegForm(data = drug_cat_rec_dict)
        print(drug_cat_form)
        return render (request, "drug_cat_update.html", {'productsCatForm': drug_cat_form})
    except:
        print(Exception)
        print("Errors", sys.exc_info())
        return render(request, 'drug_cat_update.html',{'drug_cat_recs_error': "Could not Fetch"})
    
##Delete Category
def drug_category_update(request):
    if request.method == "GET":
        productCategoryForm = DrugCategoryRegForm()
        return render (request, "drug_cat_update.html", {'productsCatForm': productCategoryForm})

    elif request.method == "POST" and request.is_ajax:
        productsCatForm = DrugCategoryRegForm(data = request.POST)
        try:
            if productsCatForm.is_valid():    
                item_cat_id = int(request.POST.get("item_cat_id", False))
                print("ITEM IDNBDDHDHDHDHDH")
                print(item_cat_id)
                edit_cat_drug =  ProductType.objects.get(id = item_cat_id)
                edit_cat_drug.name = request.POST.get("drug_category_name", False)
                edit_cat_drug.description = request.POST.get("drug_category_description", False)
                edit_cat_drug.save()
                response_data = {'recieved': True, 'status': "ok"}
                return JsonResponse(response_data)
            else:
                print("ESSSSSSSSSSSSSSSSSSSSS")
                print(Exception)
                raise Exception
        except:
            print("Errors", sys.exc_info())
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)

        productsCatForm = DrugCategoryRegForm()
        return render (request, "drug_cat_update.html", {'productsCatForm': productsForm}) 
#Delete Drug Category
class DrugCategoryDelete(DeleteView):
    model = ProductType
    # needs to match the name of the view i want to send the user back to
    template_name = "products_category_confirm_delete.html"
    success_url = reverse_lazy('inventory:display_drug_categories')



######################DRUGS#########################
##Drug registrations
def drug_reg(request):
    if request.method == "GET":
        productsForm = ProductsForm()
        return render (request, "new_drug.html", {'productsForm': productsForm})

    elif request.method == "POST" and request.is_ajax:
        productsForm = ProductsForm(data = request.POST)
        if productsForm.is_valid():
            item_name = request.POST.get("item_name", False)
            item_type = request.POST.get("item_type", False)
            brand_name = request.POST.get("brand_name", False)
            chemical_name = request.POST.get("chemical_name", False)
            receiving_name  =  request.POST.get("receiving_name", False)
            receiving_number =  request.POST.get("receiving_number", False)
            dispensing_name =  request.POST.get("dispensing_name", False)
            dispensing_number =  request.POST.get("dispensing_number", False)
            print(item_type)
            item_type_object = ProductType.objects.get(id = item_type)
            drug_reg_data = Products(item_name = item_name, item_type = item_type_object, 
             brand_name = brand_name , chemical_name = chemical_name, receiving_name = receiving_name,receiving_number = receiving_number,dispensing_name = dispensing_name,dispensing_number = dispensing_number)
            drug_reg_data.save()
            response_data = {'recieved': True, 'status': "ok"}
            return JsonResponse(response_data)
        else:
            print(productsForm)
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)
    else:
        productsForm = ProductsForm()
        return render (request, "new_drug.html", {'productsForm': productsForm})
#display all registered drugs
def display_drugs(request):
    
    try:
        drug_recs = Products.objects.all()
        print("happened")
        print(drug_recs)
        return render(request, 'drug_lists.html',{'drug_recs': drug_recs})
    except:
        print("Errors", sys.exc_info()[0])
        return render(request, 'drug_lists.html',{'drug_recs_error': "Could not Fetch"})
##Display drug individual detail
def drug_detail(request, pk):
    try:
        drug_rec = Products.objects.get(id = pk)

        item_name = drug_rec.item_name
        item_type = drug_rec.item_type.id 
        brand_name = drug_rec.brand_name
        chemical_name = drug_rec.chemical_name
        receiving_name = drug_rec.receiving_name
        receiving_number = drug_rec.receiving_number
        dispensing_name = drug_rec.dispensing_name
        dispensing_number = drug_rec.dispensing_number
        item_id =  drug_rec.id 
        drug_rec_dict = {'item_name':item_name, "item_type":item_type,"brand_name":brand_name, 
        "chemical_name": chemical_name, "item_id": item_id, "receiving_name": receiving_name,
"receiving_number": receiving_number,
"dispensing_name": dispensing_name,
"dispensing_number": dispensing_number}
        print(drug_rec.item_type.id)
        drug_form = ProductsFormUpdate(data = drug_rec_dict)
        return render (request, "drug_update.html", {'productsForm': drug_form})
    except:
        return render(request, 'drug_update.html',{'drug_recs_error': "Could not Fetch"})
##Update all drugs
def drug_update(request):
    if request.method == "GET":
        productsForm = ProductsFormUpdate()
        return render (request, "drug_update.html", {'productsForm': productsForm})

    elif request.method == "POST" and request.is_ajax:
        productsForm = ProductsFormUpdate(data = request.POST)
        try:
            if productsForm.is_valid():    
                item_id = int(request.POST.get("item_id", False))
                print("ITEM IDNBDDHDHDHDHDH")
                print(item_id)
                edit_drug =  Products.objects.get(id = item_id)
                edit_drug.item_name = request.POST.get("item_name", False)
                item_type = request.POST.get("item_type", False)
                edit_drug.brand_name = request.POST.get("brand_name", False)
                edit_drug.chemical_name = request.POST.get("chemical_name", False)
                edit_drug.receiving_name = request.POST.get("receiving_name", False)
                edit_drug.receiving_number = request.POST.get("receiving_number", False)
                edit_drug.dispensing_name = request.POST.get("dispensing_name", False)
                edit_drug.dispensing_number = request.POST.get("dispensing_number", False)
                item_type_object = ProductType.objects.get(id = item_type)
                edit_drug.item_type = item_type_object
                edit_drug.save()
                response_data = {'recieved': True, 'status': "ok"}
                return JsonResponse(response_data)
            else:
                print("ESSSSSSSSSSSSSSSSSSSSS")
                print(Exception)
                raise Exception
        except:
            print("Errors", sys.exc_info())
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)

        productsForm = ProductsFormUpdate()
        return render (request, "drug_update.html", {'productsForm': productsForm})    

## Delete Drugs
class DrugDelete( DeleteView):
    model = Products
    # needs to match the name of the view i want to send the user back to
    template_name = "products_confirm_delete.html"
    success_url = reverse_lazy('inventory:display_drugs')

#Register Store
def store_reg(request):
    if request.method == "GET":
        storeRegForm = StoreRegForm()
        return render (request, "new_store.html", {'storeRegForm': storeRegForm})

    elif request.method == "POST" and request.is_ajax:
        storeRegForm = StoreRegForm(data = request.POST)
        if storeRegForm.is_valid():
            storename = request.POST.get("storename", False)
            store_reg_data = Stores(storename = storename)
            store_reg_data.save()
            response_data = {'recieved': True, 'status': "ok"}
            return JsonResponse(response_data)
        else:
            print(storeRegForm)
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)
    else:
        storeRegForm = StoreRegForm()
        return render (request, "new_store.html", {'storeRegForm': storeRegForm})


## Display Store List
def display_stores(request):
    try:
        store_recs = Stores.objects.all()
        print("happened")
        print(store_recs)
        return render(request, 'store_lists.html',{'store_recs': store_recs})
    except:
        print("Errors", sys.exc_info()[0])
        return render(request, 'drug_lists.html',{'store_recs_error': "Could not Fetch"})
# Show Store Detail
def store_detail(request, pk):
    try:
        store_rec = Stores.objects.get(id = pk)

        storename = store_rec.storename
        
        store_id =  store_rec.id 
        store_rec_dict = {'storename':storename, "store_id":store_id}
        store_form = StoreRegForm(data = store_rec_dict)
        return render (request, "store_update.html", {'storeForm': store_form})
    except:
        return render(request, 'store_update.html',{'store_recs_error': "Could not Fetch"})
## Update Store
def store_update(request):
    if request.method == "GET":
        storeForm = StoreRegForm()
        return render (request, "store_update.html", {'storeForm': storeForm})

    elif request.method == "POST" and request.is_ajax:
        storeForm = StoreRegForm(data = request.POST)
        try:
            if storeForm.is_valid():    
                store_id = int(request.POST.get("store_id", False))
                print("ITEM IDNBDDHDHDHDHDH")
                print(store_id)
                edit_store =  Stores.objects.get(id = store_id)
                edit_store.storename = request.POST.get("storename", False)
                edit_store.save()
                response_data = {'recieved': True, 'status': "ok"}
                return JsonResponse(response_data)
            else:
                print("ESSSSSSSSSSSSSSSSSSSSS")
                print(Exception)
                raise Exception
        except:
            print("Errors", sys.exc_info())
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)

        productsForm = ProductsFormUpdate()
        return render (request, "drug_update.html", {'productsForm': productsForm}) 
#Store Delete
class StoreDelete(DeleteView):
    model = Stores
    # needs to match the name of the view i want to send the user back to
    template_name = "stores_confirm_delete.html"
    success_url = reverse_lazy('inventory:display_stores')


##Inventory 

######################DRUGS#########################
def inventory_reg(request):
    try:
        if request.method == "POST" and request.is_ajax:
            store = int(request.POST.get("store", False))
            print(store)
            quantity =  request.POST.get("quantity", False)
            product_id = int(request.POST.get("product_id", False))
            entry_product = Products.objects.get(id = product_id)
            entry_store = Stores.objects.get( id = store)
            inventory = Inventory(product = entry_product, store = entry_store, quantity = quantity )
            inventory.save()
            response_data = {'recieved': True, 'status': "ok"}
            return JsonResponse(response_data)
            
        else:
                response_data = {'recieved':False, 'status': "error"}
                return JsonResponse(response_data)
    except IntegrityError:
        print("Integrity Error Happening")
        print(IntegrityError)
        response_data = {'recieved':False, 'status': "error", "error_type": "integrity_error"}
        return JsonResponse(response_data)
    except:
        print("Overall Exceprion")
        print("Errors", sys.exc_info())
        # print(Exception)
        response_data = {'recieved':False, 'status': "error", "error_type": "other_error"}
        return JsonResponse(response_data)

def inventory_store_list(request):
    try:
        store_recs = Stores.objects.all()
        print("happened")
        print(store_recs)
        return render(request, 'store_list_drug.html',{'store_recs': store_recs})
    except:
        print("Errors", sys.exc_info()[0])
        return render(request, 'store_list_drug.html',{'store_recs_error': "Could not Fetch"})
def inventory_drug_list(request, store_id):
    ##First Templates
    display_template = {}
    display_list = []
    try:
        ##Get store needed
        store_request =  Stores.objects.get(id = store_id)
        store_name =  store_request.storename
        drugs_in_store =  Inventory.objects.filter(store = store_request)
        print("Drugs in store")
        # print(drugs_in_store[0].product.chemical_name)
        ## Feed data into display list using template from store
        for drug in drugs_in_store:
            display_template["quantity"] = drug.quantity
            display_template["chemical_name"] = drug.product.chemical_name
            display_template["item_name"] = drug.product.item_name
            display_template["brand_name"] = drug.product.brand_name
            # display_template["in_store"] = "present"
            display_template["drug_id"] = drug.product.id
            display_list.append(display_template)
            print("Drugs in store")
            display_template = {}
        ##Get data not in store and use template to feed in display list

        drugs_not_in_store =  Products.objects.filter(inventory__isnull = True)
        for drug in drugs_not_in_store:
            print("drugs not in store metioned")
            display_template["quantity"] = "Not in Store"
            display_template["chemical_name"] = drug.chemical_name
            display_template["item_name"] = drug.item_name
            display_template["brand_name"] = drug.brand_name
            # display_template["in_store"] ="Not in Store"
            display_template["drug_id"] = drug.id
            display_list.append(display_template)
            display_template = {}    
        ##Paginate the display list 
        page = request.GET.get('page', 1)
        paginator = Paginator(display_list,10)
    
        drug_recs = paginator.page(page)
        return render(request, 'inventory_drug_list.html', {'drug_recs':drug_recs,'store_name':store_name})

    except PageNotAnInteger:
        drug_recs = paginator.page(1)
        return render(request, 'inventory_drug_list.html', {'drug_recs':drug_recs,'store_name':store_name})

    except EmptyPage:
        drug_recs = paginator.page(paginator.num_pages)
        return render(request, 'inventory_drug_list.html', {'drug_recs':drug_recs,'store_name':store_name})
    
    except:
        print("Drugs not in store", sys.exc_info()[0])
        return render(request, 'inventory_drug_list.html', {'drug_recs_error':"drug_recs_error",'store_name':store_name})



# Display Form and also Product Detail
def inventory_detail(request,pk):
    try:
        product = Products.objects.get(id = pk)
        stores_present = Inventory.objects.filter(product = product)
        store_pres_id = []
        for store_pres in stores_present:
            store_pres_id.append(store_pres.store.id)
        stores_absent = Stores.objects.exclude(id__in = store_pres_id)
        print("stores_ab")
        print(stores_absent)
            # print(store_pres.store.id)
        # stores_absent = Inventory.objects.filter(store_isnull= True)
        print(store_pres_id)
        # stores_absent =  Stores.objects.filter(inventory__isnull = True)
        stores_absent_list = [(store.id, store.storename) for store in stores_absent]
        assignStoreForm = AssignStoreForm(stores_absent_list, product.id)
        quantity_template = {}
        quantity_list =  []
        # print(stores_absent)
        # QuantityUpdateFormset = formset_factory(UpdateQauntityForm, extra = len(stores_present) )
        # quantityUpdateFormset = QuantityUpdateFormset()
        product_common_name = product.item_name
        product_brand_name = product.brand_name
        product_chemical_name = product.chemical_name
        product_detail = {"product_common_name":product_common_name ,"product_brand_name":product_brand_name ,"product_chemical_name":product_chemical_name}
        for store in stores_present:
            quantity_template = {"store_name":store.store.storename, "quantity": store.quantity, "store_id":store.id}
            quantity_list.append(quantity_template)
            quantity_template = {}
        
        print(quantity_list)
        print("inventory_detail")
        # print(assignStoreForm)
        return render(request, "inventory_adjustment.html", {"product_detail":product_detail,"assignStoreForm": assignStoreForm, "quantity_recs":quantity_list})
    except:
        # print(Exception)
        print("Errors", sys.exc_info()[0])
        return render(request, 'inventory_adjustment.html', {'display_errors':"display_errors"})

def inventory_quantity_detail(request, pk):
    try:
        inventory = Inventory.objects.get(id = pk)
        inventory_id =  pk
        product_id = inventory.product.id 
        product_common_name = inventory.product.item_name
        product_brand_name = inventory.product.brand_name
        product_chemical_name = inventory.product.chemical_name
        store_name = inventory.store.storename
        store_id = inventory.store.id
        quantity = inventory.quantity
        updateData = {"store_id":store_id,"product_id":product_id,"quantity": quantity}
        product_details = {"product_common_name":product_common_name,"product_brand_name":product_brand_name,"product_chemical_name": product_chemical_name, "store_name":store_name}
        updateQuantityForm = UpdateQauntityForm(data = updateData)
        return render (request, "inventory_quantity_update.html", {"inventory_id":inventory_id,"product_detail":product_details,"updateQuantityForm":updateQuantityForm})
    except:
        # print(Exception)
        print("Errors", sys.exc_info()[0])
        return render(request, 'inventory_quantity_update.html', {'quantity_errors':"errors"})
def inventory_quantity_update(request):
    if request.method == "POST" and request.is_ajax:
        updateQuantityForm = UpdateQauntityForm(data = request.POST)
        try:
            if updateQuantityForm.is_valid():    
                store_id = int(request.POST.get("store_id", False))
                print("Store Id")
                print(store_id)
                prod_id = int(request.POST.get("product_id", False))
                print("Prod Id ")
                print(prod_id)
                prod_present= Products.objects.get(id = prod_id)
                store_present =  Stores.objects.get(id = store_id)
                edit_inventory =  Inventory.objects.get(product = prod_present, store =  store_present)
                edit_inventory.quantity = request.POST.get("quantity", False)            
                edit_inventory.save()
                response_data = {'recieved': True, 'status': "ok"}
                return JsonResponse(response_data)
            else:
                print("ESSSSSSSSSSSSSSSSSSSSS")
                print(Exception)
                raise Exception
        except:
            print("Errors", sys.exc_info())
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)

def inventory_delete(request, pk):
    try:
        inv_rec =  Inventory.objects.get(id = pk)
        prod_id = inv_rec.product.id
        inv_rec.delete()
        url_to_fallback = 'inventory:inventory_drug_list'+str(prod_id)
        return redirect("inventory:inventory_detail" ,prod_id)
    except:
            print("Errors", sys.exc_info())
            response_data = {'deleted':False, 'status': "error"}
            return JsonResponse(response_data)
# class InventoryDelete(DeleteView):
#     model = Inventory
    
#     # def get_context_data(self, **kwargs) :
#     #     global stid 

#     #     context = super().get_context_data(**kwargs)
#     #     print("putting id")
#     #     stid2=context['inventory'].store.id
#     #     return context
#     #print(stid)
#     template_name = "inventory_confirm_delete.html"
#     # get_context_data())["inventory"].store.id
#     # url_to_fallback = 'inventory:inventory_drug_list'
#     def get_success_url(self):
#         # store_id = self.kwargs["store_id"]
#         # return super().get_success_url()
#         print("sekf kwargs")
#         print(self.kwargs)
#         # store_id = self.kwargs["pk"]
#         pk = self.kwargs["pk"]
#         # return reverse('inventory:inventory_drug_list', kwargs={"store_id":store_id})
#         return reverse('inventory:inventory_detail', kwargs={"pk":pk})

    # success_url = reverse_lazy('inventory:inventory_drug_list')

### SUPPLIER CRUD
#Register Supplier
def supplier_registration(request):
    if request.method == "GET":
        supplierRegForm = SupplierRegForm()
        return render (request, "new_supplier.html", {'supplierRegForm': supplierRegForm})

    elif request.method == "POST" and request.is_ajax:
        supplierRegForm = SupplierRegForm(data = request.POST)
        if supplierRegForm.is_valid():
            supplier_name = request.POST.get("supplier_name", False)
            supplier_email = request.POST.get("supplier_email", False)
            supplier_phone = request.POST.get("supplier_phone", False)
            supplier_reg_data = Suppliers(name = supplier_name, email = supplier_email,  phone = supplier_phone )
            supplier_reg_data.save()
            response_data = {'recieved': True, 'status': "ok"}
            return JsonResponse(response_data)
        else:
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)
    else:
        supplierRegForm = SupplierRegForm()
        return render (request, "new_supplier.html", {'supplierRegForm': supplierRegForm})
    

#display all registered drugs
def display_suppliers(request):
    
    try:
        supplier_recs = Suppliers.objects.all()
        return render(request, 'supplier_lists.html',{'supplier_recs': supplier_recs})
    except:
        print("Errors", sys.exc_info()[0])
        return render(request, 'supplier_lists.html',{'supplier_recs_error': "Could not Fetch"})
## Supplier Detail Display
def supplier_detail(request, pk):
    try:
        supplier_rec = Suppliers.objects.get(id = pk)

        supplier_name = supplier_rec.name
        supplier_email = supplier_rec.email
        supplier_phone = supplier_rec.phone
        supplier_id = supplier_rec.id
        supplier_rec_dict = {'supplier_name':supplier_name, "supplier_email":supplier_email, "supplier_phone":supplier_phone,"supplier_id":supplier_id}
        supplierForm = SupplierRegForm(data = supplier_rec_dict)
        return render (request, "supplier_update.html", {'supplierForm': supplierForm})
    except:
        return render(request, 'supplier_update.html',{'supplier_rec_error': "Could not Fetch"})

#Supplier Update
def supplier_update(request):
    if request.method == "GET":
        suppplierForm = SupplierRegForm()
        return render (request, "supplier_update.html", {'suppplierForm': suppplierForm})

    elif request.method == "POST" and request.is_ajax:
        suppplierForm = SupplierRegForm(data = request.POST)
        try:
            if suppplierForm.is_valid():    
                
                print("suppllierr form ")
                print(request.POST)
                supplier_id = int(request.POST.get("supplier_id", False))
                edit_supplier =  Suppliers.objects.get(id = supplier_id)
                edit_supplier.name = request.POST.get("supplier_name", False)
                edit_supplier.email = request.POST.get("supplier_email", False)
                edit_supplier.phone = request.POST.get("supplier_phone", False)
                edit_supplier.save()
                response_data = {'recieved': True, 'status': "ok"}
                return JsonResponse(response_data)
            else:
                print("ESSSSSSSSSSSSSSSSSSSSS")
                print(Exception)
                raise Exception
        except:
            print("Errors", sys.exc_info())
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)

        suppplierForm = SupplierRegForm()
        return render (request, "supplier_update.html", {'suppplierForm': suppplierForm})
#Supplier Delete
class SupplierDelete(DeleteView):
    model = Suppliers
    # needs to match the name of the view i want to send the user back to
    template_name = "suppliers_confirm_delete.html"
    success_url = reverse_lazy('inventory:display_suppliers')

#External order
##Create e
def create_external_order(request):
    if request.method == "GET": 
        createExternalOrderForm=CreateExternalOrderForm()
        return render(request, "create_external_order.html", {"createExternalOrderForm":createExternalOrderForm})
    if request.method == "POST" and request.is_ajax:
        createExternalOrderForm = CreateExternalOrderForm(data = request.POST)
        try: 
            if createExternalOrderForm.is_valid:
                invoice_number = request.POST.get("invoice_number", False)
                supplier_id  = request.POST.get("supplier", False)  
                destination_store_id = request.POST.get("destination_store", False)
                destination_store =  Stores.objects.get(id = int(destination_store_id))
                supplier = Suppliers.objects.get(id = int(supplier_id))

                externalOrder=ExternalOrder(supplier = supplier, invoice_number = invoice_number,
                destination_store = destination_store, total_invoiced_amount = 0.0,date_time_entry = str(timezone.now()) 
                , user_involved = request.user, approver = request.user )
                externalOrder.save()
            response_data = {'recieved': True, 'status': "ok"}
            return JsonResponse(response_data)

        except:
            print("create_external_order", sys.exc_info())
            response_data = {'recieved':False, 'status': "error"}
            return JsonResponse(response_data)

#display all registered drugs
def display_external_orders(request):
    
    try:
        external_order_recs = ExternalOrder.objects.all()
        return render(request, 'external_order_lists.html',{'external_order_recs': external_order_recs})
    except:
        print("Errors", sys.exc_info()[0])
        return render(request, 'external_order_lists.html',{'external_order_recs_error': "Could not Fetch"})
def external_order_detail(request, pk):
    try:
        external_order_rec = ExternalOrder.objects.get(id = pk)
        external_order_id = external_order_rec.id
        invoice_number = external_order_rec.invoice_number
        supplier = external_order_rec.supplier
        destination_store = external_order_rec.destination_store
        total_invoiced_amount = external_order_rec.total_invoiced_amount
        date_time_entry = external_order_rec.date_time_entry
        approval = external_order_rec.approval
        products = external_order_rec.products
        table_data = []
        drugIntakeForm =  DrugIntakeForm()
        if products == None:
            print("prducts"+ str(type(products)))
        else:
            external_order_data_frame =  pd.DataFrame.from_dict(products, orient = 'index')
            # print(external_order_data_frame["brand_name"])
            p= 1
            for i in products:
                products[i]["count"] = p
                table_data.append(products[i])
                p =p+1
            print(table_data)


        external_info_dict = {'external_order_id':external_order_id, "invoice_number":invoice_number, 
        "supplier":supplier,"destination_store":destination_store, "total_invoiced_amount":total_invoiced_amount,
        "date_time_entry": date_time_entry,"approval":approval}
        
        # supplierForm = SupplierRegForm(data = supplier_rec_dict)
        return render (request, "external_order_update.html",{"table_data":table_data,'drugIntakeForm': drugIntakeForm, "external_info_dict":external_info_dict})
    except:
        print("External Update Error", sys.exc_info())
        return render(request, 'external_order_update.html',{'external_info_error': "Could not Fetch"})
def external_order_update(request):
    ###Get details of order 
    externalOrderForm = CreateExternalOrderForm()
    # ExternalOrderFormset = formset_factory(CreateExternalOrderForm, )
    ###Update inventory
    
    
    
    if request.method == "POST" and request.is_ajax:
        external_order_template = {}
        item_name_list =  request.POST.getlist("item_name", False)
        receiving_number_list =  request.POST.getlist("receiving_number", False)
        dispensing_number_list =  request.POST.getlist("dispensing_number", False)
        brand_name_list =  request.POST.getlist("brand_name", False)
        chemical_name_list =  request.POST.getlist("chemical_name", False)
        receiving_name_list =  request.POST.getlist("receiving_name", False)
        drug_id_list =  request.POST.getlist("drug_id", False)
        quantity_list =  request.POST.getlist("quantity", False)
        total_price_list =  request.POST.getlist("total_price", False)
        external_order_id = request.POST.get("external_order_id",False)
        price_list =  request.POST.getlist("price",False)
        print("prce list")
        print(price_list[0])
        #Get the record to update
        external_order = ExternalOrder.objects.get(id = external_order_id)
        print(external_order_id)
        for d in range(0, len(item_name_list)):
            count =str( d+1)
            print("count = "+count)
            external_order_template["Drug"+count]= {"item_name": item_name_list[d], 
                "receiving_number":receiving_number_list[d],
                "dispensing_number":dispensing_number_list[d],
                "brand_name":brand_name_list[d],
                "chemical_name":chemical_name_list[d],
                "receiving_name":receiving_name_list[d],
                "drug_id":drug_id_list[d],
                "quantity":quantity_list[d],
                "price":price_list[d],

                "total_price":total_price_list[d]}
        external_order.products = external_order_template
        external_order.save()

    # invoice_number
    # supplier
    # destination_store
    # total_invoiced_amount
    # date_time_entry
    # user_involved
    # approval
    # approver
    # products



