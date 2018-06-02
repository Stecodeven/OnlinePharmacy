$(document).ready(function(){

	$(".check").click( function(){
		var list = $(".check");

        var i = 0;
        for(;i<(list.size()-1);i++) {
            //console.log(list[i].checked);
            if(list[i].checked == false) {
                //console.log("12");
                $("#J_SelectAllCbx2").attr("checked",false);
                break;
            }
        }
        if(i >= (list.size() - 1))$("#J_SelectAllCbx2").attr("checked","checked");
        var id = this.id;
        var cid = "#c_" + id, pid = "#p_" + id;
        var count = Number( $(cid).val() ), price=parseFloat( $(pid).text() );
        var c_now = $("#J_SelectedItemsCount").text();
        var p_now = $("#J_Total").text();

        if(this.checked == true) {
            c_now = Number(c_now) + count;
            p_now = parseFloat(p_now) + count * price;
        }else {
            c_now = Number(c_now) - count;
            p_now = parseFloat(p_now) - count * price;
        }
        $("#J_SelectedItemsCount").text(c_now);
        $("#J_Total").text(p_now.toFixed(2));

        if(c_now == 0) {

        }
	});



});