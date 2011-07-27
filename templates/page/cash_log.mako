<%inherit file="/main.mako"/>
<%!
    from app.utils.currency import formatcurrency
    import app.utils.date as dateutils
%>
<%
    runningsum = 0
    balance_str = escape(formatcurrency(balance))
%>
<h1>Kasselog</h1>
<table style="width:100%;">
    <thead>
        <tr>
            <th>Tidspunkt</th>
            <th>Beskrivelse</th>
            <th>Ændring</th>
            <th>Saldo</th>
        </tr>
    </thead>
    <tbody>
%for date, description, amount in log:
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    date_str = escattr(date.strftime("%d/%m-%Y %H:%M:%S"))
    description = escape(description)
    amount_str = escape(formatcurrency(amount))
    runningsum += amount
    runningsum_str = escape(formatcurrency(runningsum))
%>
        <tr>
            <td title=${date_str}>${date_delta}</td>
            <td>${description}</td>
            <td style="text-align:right;">${amount_str}</td>
            <td style="text-align:right;">${runningsum_str}</td>
        </tr>
%endfor
        <tr style="border-top:3px solid #000;">
            <td colspan="2">Balance</td>
            <td style="text-align:right;" colspan="2">${balance_str}</td>
        </tr>
    </tbody>
</table>
<h3>Justér kassebeholdning</h3>
<p>Skriv hvor meget du lægger i (plus) eller tager (minus) fra kassen.</p>
<form method="post" action=${escattr(urlfor("misc.adjust_cash"))}>
    <label for="amount">Beløb:</label> <input type="text" id="amount" name="amount" />
</form>
