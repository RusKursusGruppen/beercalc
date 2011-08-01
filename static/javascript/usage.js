function preview_update(){
    $.post(preview_url,
        $("#usage_form").serialize(),
        function(data){
            var total = 0;
            data.accounts.forEach(function(account){
                $("#preview_" + account.id).text(formatcurrency(account.balance));
                total += account.balance;
            });
            $("#preview_total").text(formatcurrency(total));
            data.prices.forEach(function(product){
                $("#price_" + product.id).text(formatcurrency(product.price));
            });
        },
        "json"
    );

    product_ids.forEach(function(pid) {
        var usage = 0;
        account_ids.forEach(function(aid) {
            usage += parseInt($("input[name=usage_"+aid+"_"+pid+"]").val());
        });
        $("#total_"+pid).text(formatnumber(usage));
    });
}
function check_form(){
    if ($("#usage_form .stock").val() == ""){
        $("#stock_error").text("Du har glemt at indføre en beholdning.").show();
        return false;
    }
    return true;
}

$(document).ready(function(){
    preview_update();
    $("#usage_form input[type=text]").keyup(preview_update);
    $("#usage_form").submit(check_form);
});
