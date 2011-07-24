<%!
import app.utils.date as dateutils
from app.utils.misc import formatcurrency
%>
<%inherit file="/main.mako"/>
<h1>${name}</h1>

<table>
    <thead>
        <tr>
            <th>Dato</th>
            <th>Beskrivelse</th>
            <th>Amount</th>
        </tr>
    </thead>
    <tbody>
%for date, description, amount in transactions:
<%
    date = escape(dateutils.formatdelta(date-dateutils.now()))
    description = escape(description)
    amount = escape(formatcurrency(amount))
%>
        <tr>
            <td>${date}</td>
            <td>${description}</td>
            <td style="text-align:right;">${amount}</td>
        </tr>
%endfor
    </tbody>
</table>
