<%!
    from app.utils.currency import formatcurrency
%><%
    response.headers["Content-Type"] = "application/json; charset=UTF-8"
    from json import dumps

    accounts_dict = list({"id": x[0], "balance": formatcurrency(-x[1])} for x in accounts)
%>${dumps(accounts_dict)}
