$(function(){
// DRUG CATEGORY CRUD
//Category data submission
    $("#submit_drug_category_data").click(function(e){
        e.preventDefault();
        new_drug_category_data = $('#new_drug_category_form').serialize();
        $.ajax({
            type: "POST",
            url:"/inventory/drug_category_reg",
            data:new_drug_category_data,
            beforeSend:function(){
                // alert("beforeSend");

            },
            cache: false,
            dataType: "json",
            success: function(data){
                //alert(new_drug_category_data);
                if (data.status === "ok"){
                    $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Drug Category Successfuly saved. </div></div>");
                    $("#new_drug_category_form")[0].reset();
                }
                if (data.status === "error"){
                    $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

                }
                
            }
        });
        return false
    });

//Update Drug Category
$("#submit_drug_cat_update_data").click(function(e){
    e.preventDefault();
    update_drug_category_data = $('#update_drug_cat_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/drug_category_update",
        data:update_drug_category_data,
        beforeSend:function(){
            alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Drug Data Successfuly Updated. </div></div>");
                // $("#new_drug_form")[0].reset();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

//DRUG CRUD

//New Drug Registration
$("#submit_drug_data").click(function(e){
    e.preventDefault();
    new_drug_category_data = $('#new_drug_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/drug_reg",
        data:new_drug_category_data,
        beforeSend:function(){
            // alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Drug Data Successfuly saved. </div></div>");
                $("#new_drug_form")[0].reset();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

//Update Drugs
$("#submit_drug_update_data").click(function(e){
    e.preventDefault();
    new_drug_category_data = $('#update_drug_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/drug_update",
        data:new_drug_category_data,
        beforeSend:function(){
            // alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Drug Data Successfuly Updated. </div></div>");
                // $("#new_drug_form")[0].reset();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

// STORE CRUD

//New Store Registration
$("#submit_store_data").click(function(e){
    e.preventDefault();
    new_store_data = $('#new_store_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/store_reg",
        data:new_store_data,
        beforeSend:function(){
            alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Drug Data Successfuly saved. </div></div>");
                $("#new_store_form")[0].reset();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

//Update Store
$("#submit_store_update_data").click(function(e){
    e.preventDefault();
    update_store_data = $('#update_store_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/store_update",
        data:update_store_data,
        beforeSend:function(){
            // alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Store Data Successfuly Updated. </div></div>");
                // $("#new_drug_form")[0].reset();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});


//Inventory CRUD

//New Inventory Registration
$("#submit_new_store_data").click(function(e){
    e.preventDefault();
    new_inventory_data = $('#new_data_inventory_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/inventory_reg",
        data:new_inventory_data,
        beforeSend:function(){
            // alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Inventory Data Successfuly saved. </div></div>");
                // $("#new_inventory_form")[0].reset();
                location.reload();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

//Update Inventory 
$("#submit_inventory_update_data").click(function(e){
    e.preventDefault();
    new_drug_category_data = $('#update_inventory_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/inventory_quantity_update",
        data:new_drug_category_data,
        beforeSend:function(){
            // alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            //alert(new_drug_category_data);
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Drug Inventory Successfuly Updated. </div></div>");
                // $("#new_drug_form")[0].reset();
                location.reload();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

//SUPPLIER CRUD 

//New Supplier Registration
$("#submit_supplier_data").click(function(e){
    e.preventDefault();
    new_supplier_data = $('#new_supplier_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/supplier_registration",
        data:new_supplier_data,
        beforeSend:function(){
             alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            alert("new_drug_category_data");
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Supplier Data Successfuly saved. </div></div>");
                $("#new_supplier_form")[0].reset();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});

//Update Supplier Info
$("#submit_supplier_update_data").click(function(e){
    e.preventDefault();
    new_supplier_data = $('#update_supplier_form').serialize();
    $.ajax({
        type: "POST",
        url:"/inventory/supplier_update",
        data:new_supplier_data,
        beforeSend:function(){
            alert("beforeSend");

        },
        cache: false,
        dataType: "json",
        success: function(data){
            alert("sending");
            if (data.status === "ok"){
                $("#my_alert_box").append("<div class='alert alert-success alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button>Supplier Info Successfuly Updated. </div></div>");
                // $("#new_drug_form")[0].reset();
                // location.reload();
            }
            if (data.status === "error"){
                $("#my_alert_box").append("<div class='alert alert-danger alert-dismissable'><button aria-hidden='true' data-dismiss='alert' class='close' type='button'> × </button> Error! Please check your data again </div></div>");

            }
            
        }
    });
    return false
});



});