<%
    response.headers["Content-Type"] = "application/json; charset=UTF-8"

    accounts_list = list({"id": x[0], "balance": -x[1]} for x in accounts)
    prices_list = list({"id": x[0], "price": -x[1]} for x in prices)

    data = {"accounts": accounts_list, "prices": prices_list}
%>${json(data)}
