<%inherit file="/main.mako"/>
<%!
    from app.utils.currency import formatcurrency
%>
<%
    self.breadcrumbs = (
        (urlfor("misc.cashlog"), u"Kassebeholdning"),
    )
    runningsum = 0
    balance_str = escape(formatcurrency(balance))
%>
<h1>Kasselog</h1>
<table class="transaction_log">
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
    description = escape(description)
    amount_str = escape(formatcurrency(amount))
    runningsum += amount
    runningsum_str = escape(formatcurrency(runningsum))
%>
        <tr>
            <td>${widget.timedelta(date)}</td>
            <td>${description}</td>
            <td class="money">${amount_str}</td>
            <td class="money">${runningsum_str}</td>
        </tr>
%endfor
        <tr class="summary">
            <td colspan="2">Balance</td>
            <td class="money" colspan="2">${balance_str}</td>
        </tr>
    </tbody>
</table>
<h3>Justér kassebeholdning</h3>
<p>Skriv hvor meget du lægger i (plus) eller tager (minus) fra kassen.</p>
<form method="post" action=${escattr(urlfor("misc.adjust_cash"))}>
    <label for="amount">Beløb:</label> <input type="text" id="amount" name="amount" />
</form>
