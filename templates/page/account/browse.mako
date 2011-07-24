<%inherit file="/main.mako"/>
<%!
from app.utils.misc import formatcurrency
%>
<h1>Konti</h1>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Saldo</th>
        </tr>
    </thead>
    <tbody>
%for id, name, balance in accounts:
        <tr>
            <td><a href=${escattr(url_for("account.edit", id=id))}>${escape(name)}</td>
            <td style="text-align:right;">${escape(formatcurrency(balance))}</td>
        </tr>
%endfor
    </tbody>
</table>
