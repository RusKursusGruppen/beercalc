function preview_update(){
    $.post(preview_url,
        $("#usage_form").serialize(),
        function(accountlist){
            accountlist.forEach(function(account){
                $("#preview_" + account.id).text(account.balance);
            });
        },
        "json"
    );
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
