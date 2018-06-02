$(document).ready(function(){
	
	$("#LikBasket").click( function(){
		
		var count = $("#text_box").val();
		var p_id = "{{pid}}";

		var csrf = $('input[name="csrfmiddlewaretoken"]').val()


        console.log(count + "  " + p_id + "  " + csrf);

		params = {'p_id':p_id, 'count':count, 'csrfmiddlewaretoken':csrf}

		$.post('/cart/add/', params, function (data) {
		    console.log(data.message);
			$('#J_MiniCartNum').text(data.cart_count);
		});
	});
	
	
});