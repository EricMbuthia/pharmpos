"""pharmpos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path


app_name = "inventory"
urlpatterns = [
    ###Drugs Category CRUD
    path('drug_category_reg', views.drug_category_reg, name = 'drug_category_reg'),
    path('display_drug_categories', views.display_drug_categories, name='display_drug_categories'),
    path('drug_category_detail/<int:pk>/', views.drug_category_detail, name='drug_category_detail'),
    path('drug_category_update', views.drug_category_update, name='drug_category_update'),
    path('drug_category_delete/<pk>/', views.DrugCategoryDelete.as_view(), name = "drug_category_delete"),
    ###Drugs CRUD
    path('drug_reg', views.drug_reg, name = 'drug_reg'),
    path('display_drugs', views.display_drugs,name='display_drugs'),
    path('drug_detail/<int:pk>/', views.drug_detail,name='drug_detail'),
    path('drug_update', views.drug_update,name='drug_update'),
    path('drug_delete/<pk>/', views.DrugDelete.as_view(), name = "drug_delete"),
    ###Stores CRUD
    path('store_reg', views.store_reg, name = 'store_reg'),
    path('display_stores', views.display_stores,name='display_stores'),
    path('store_detail/<int:pk>/', views.store_detail,name='store_detail'),
    path('store_update', views.store_update,name='store_update'),
    path('store_delete/<pk>/', views.StoreDelete.as_view(), name = "store_delete"),
    ###Inventory  CRUD
    path('inventory_reg', views.inventory_reg, name = 'inventory_reg'),
    ###Need a link on interface
    path('inventory_drug_list/<store_id>', views.inventory_drug_list, name='inventory_drug_list'),
    path('inventory_detail/<int:pk>/', views.inventory_detail, name='inventory_detail'),
    path('inventory_quantity_detail/<int:pk>/', views.inventory_quantity_detail, name='inventory_quantity_detail'),
    path('inventory_quantity_update', views.inventory_quantity_update, name='inventory_quantity_update'),
    # path('inventory_delete/<pk>/', views.InventoryDelete.as_view(), name = "inventory_delete"),
    path('inventory_delete/<pk>/', views.inventory_delete, name = "inventory_delete"),


    path('inventory_store_list', views.inventory_store_list, name='inventory_store_list'),

    

    


    # path('product_detail/<int:pk>/', views.ProductDetail.as_view(), name="product_detail"),
    # path('product_update/<int:pk>/', views.ProductUpdate.as_view(), name="product_update"),

]


