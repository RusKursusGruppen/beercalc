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
    var errors = new Array();
    $("#error ul > li").remove();

    var stock_error = false;
    $("#usage_form input.stock").each(function(k, v) {
        n = parseInt($(v).val());
        if (isNaN(n) || n < 0) {
            $(v).addClass("error");
            if (!stock_error) {
                errors.push("Beholdning skal være et ikke-negativt heltal.");
                stock_error = true;
            }
        }
        else {
            $(v).removeClass("error");
        }
    });

    var usage_error = false;
    $("#usage_form input.usage").each(function(k, v) {
        val = $(v).val();
        if (val == "")
            val = "0";

        n = parseInt(val);
        if (isNaN(n) || n < 0) {
            $(v).addClass("error");
            if (!usage_error) {
                errors.push("Forbrug skal være et ikke-negativt heltal.");
                usage_error = true;
            }
        }
        else {
            $(v).removeClass("error");
        }
    });

    var profit_error = false;
    $("#usage_form input.profit").each(function(k, v) {
        if (!validatenumber($(v).val())) {
            $(v).addClass("error");
            if (!profit_error) {
                errors.push("Profit skal være et gyldigt beløb.");
                profit_error = true;
            }
        }
        else {
            $(v).removeClass("error");
        }
    });

    if (errors.length > 0) {
        errors.forEach(function(e) {
            $("#error ul").append($("<li>").text(e));
        });

        $("#error").show();
        $('html, body').stop().animate({
            scrollTop: $("#error").offset().top
        }, 500);
        return false;
    }
    return true;
}

$(document).ready(function(){
    preview_update();
    $("#usage_form input[type=text]").keyup(preview_update);
    $("#usage_form").submit(check_form);
});
