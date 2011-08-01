<%inherit file="/main.mako"/>
<%!
    from app.utils.currency import formatcurrency
    import app.utils.date as dateutils
%>
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    date_str = escattr(date.strftime("%Y-%m-%dT%H:%M:%S"))
%>
<h1>Velkommen til beercalc</h1>

<h3>Status</h3>

<table>
    <tr>
        <td>Kassebeholdning</td>
        <td>${escape(formatcurrency(cash_in_hand))}</td>
    </tr>
    <tr>
        <td>Manglende indkrævning</td>
        <td>${escape(formatcurrency(recievable_cash))}</td>
    </tr>
    <tr>
        <td>Indtægter i alt</td>
        <td>${escape(formatcurrency(income))} (heraf profit: ${escape(formatcurrency(profit))})</td>
    </tr>
    <tr>
        <td>Udgifter i alt</td>
        <td>${escape(formatcurrency(expenses))}</td>
    </tr>
    <tr>
        <td>Sidste ændring</td>
        <td><time datetime=${date_str} title=${date_str}>${date_delta}</time> (${comment})</td>
    </tr>
</table>
