$(document).ready(function(){

	$(".min").click( function(){
		var p_id = this.id;
		var csrf = $('input[name="csrfmiddlewaretoken"]').val()


        console.log(p_id + "  " + csrf);

		params = {'p_id':p_id, 'csrfmiddlewaretoken':csrf}

		$.post('#', params, function (data) {
		    console.log(data.message);
			$('#J_MiniCartNum').text(data.cart_count);
		});
	});


});