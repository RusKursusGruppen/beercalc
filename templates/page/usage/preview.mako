<%!
    from app.utils.currency import formatcurrency
    from json import dumps
%><%
    response.headers["Content-Type"] = "application/json; charset=UTF-8"

    accounts_list = list({"id": x[0], "balance": formatcurrency(-x[1])} for x in accounts)
    prices_list = list({"id": x[0], "price": formatcurrency(-x[1])} for x in prices)

    data = {"accounts": accounts_list, "prices": prices_list}
%>${dumps(data)}
