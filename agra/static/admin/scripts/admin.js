
$(function(){


	$(".edit_name").click(function(event) {
		event.preventDefault()
		var id = $(this).attr("id")
		$("#edit_name_id_" + id).toggle();
	});

	$(".name_edit_button").click(function(event){
			event.preventDefault()
			var new_id = $(this).attr("id")
			var new_name = $(".name_box#" + new_id).val()
			console.log(new_name)
			if(new_name){
				$.ajax({
					type:"POST",
					url:"/admin/products_edit/change_info",
					data: JSON.stringify({"name": new_name, "id": new_id}),
					contentType:"application/json;charset=UTF-8"
				});

				$(".name#" + new_id).text("Name: " + new_name)
				$(".name_box#" + new_id).val("")
			};
	});


	$(".edit_sku").click(function(event) {
		event.preventDefault()
		var id = $(this).attr("id")
		$("#edit_sku_id_" + id).toggle();
		
	});


	$(".sku_edit_button").click(function(event) {
			event.preventDefault()
			var new_id = $(this).attr("id")
			var new_sku = $(".sku_box#" + new_id).val().toUpperCase()
			console.log(new_sku)
			if(new_sku){
				$.ajax({
					type:"POST",
					url:"/admin/products_edit/change_info",
					data: JSON.stringify({"sku": new_sku, "id": new_id}),
					contentType:"application/json;charset=UTF-8"
				});
				$(".sku#" + new_id).text("Sku: " + new_sku)
				$(".sku_box#" + new_id).val("")
			};
	});


	$(".edit_quantity").click(function(event) {
		event.preventDefault()
		var id = $(this).attr("id")
		$("#edit_quantity_id_" + id).toggle();
	});


	$(".quantity_edit_button").click(function(event){
			event.preventDefault()
			var new_id = $(this).attr("id")
			var new_quantity = $(".quantity_box#" + new_id).val()
			console.log(new_quantity)
			if(new_quantity){
				$.ajax({
					type:"POST",
					url:"/admin/products_edit/change_info",
					data: JSON.stringify({"quantity": new_quantity, "id": new_id}),
					contentType:"application/json;charset=UTF-8"
				});
				$(".quantity#" + new_id).text("Quantity: " + new_quantity)
				$(".quantity_box#" + new_id).val("")
			};
	});



});