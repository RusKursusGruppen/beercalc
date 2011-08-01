<%!
import app.utils.date as dateutils
from app.utils.currency import formatcurrency
%>
<%inherit file="/main.mako"/>

<%
runningsum = 0
email_val = escattr(u"mailto:" + email)
email_str = escape(email)
balance_str = escape(formatcurrency(balance))
%>

<h1>
%if len(name) != 0:
    ${escape(name)}
%else:
    [Tomt Navn]
%endif
%if name in (u'Bjørn Uhre Arnholtz', u'Daniel Egeberg') and istutor:
    er nice
%endif
%if len(email) != 0:
    (<a href=${email_val}>${email_str}</a>)
%endif
</h1>
<form method="post" action=${escattr(urlfor("account.edit_do", id=id))}>
<table>
    <tr>
        <td>
            <label for="name">Navn:</label>
        </td>
        <td>
            <input name="name" id="name" value=${escattr(name)} />
        </td>
    </tr>
    <tr>
        <td>
            <label for="email">E-mail:</label>
        </td>
        <td>
            <input name="email" id="email" value=${escattr(email)} />
        </td>
    </tr>
    <tr>
        <td>
            <label for="istutor">Er rusvejleder:</label>
        </td>
        <td>
%if istutor:
            <input type="checkbox" checked="checked" name="istutor" />
%else:
            <input type="checkbox" name="istutor" />
%endif
        </td>
    </tr>
    <tr>
        <td colspan="2">
            <input type="submit" value="Gem" />
        </td>
    </tr>
</table>
</form>

<h3>Transaktioner</h3>
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
            <td><time datetime=${date_str} title=${date_str}>${date_delta}</time></td>
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
<form action=${escattr(urlfor("account.payment", id=id))} method="post">
    <label for="amount">Indtast beløb:</label>
    <input type="text" name="amount" id="amount" />
    <input type="submit" value="Indfør" />
    <p>
        Bemærk at der også kan benyttes negative beløb til hvis kontoejeren
        får penge retur.
    </p>
</form>
