<%!
import app.utils.date as dateutils
from app.utils.misc import formatcurrency
%>
<%inherit file="/main.mako"/>

<%
runningsum = 0
email_val = escattr(u"mailto:" + email)
email_str = escape(email)
balance_str = escape(formatcurrency(balance))
%>

%if len(email) == 0:
    <h1>${name}</h1>
%else:
    <h1>${name} (<a href=${email_val}>${email_str}</a>)</h1>
%endif

<h3>Transaktioner</h3>
<table>
    <thead>
        <tr>
            <th>Tidspunkt</th>
            <th>Beskrivelse</th>
            <th>Ændring</th>
            <th>Saldo</th>
        </tr>
    </thead>
    <tbody>
%for date, description, amount in transactions:
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

<h3>Indfør betaling/retur af penge</h3>
<form action="" method="post">
    <label for="amount">Indtast beløb:</label>
    <input type="text" name="amount" id="amount" />
    <input type="submit" value="Indfør" />
    <p>
        Bemærk at der også kan benyttes negative beløb til hvis kontoejeren
        får penge retur.
    </p>
</form>
