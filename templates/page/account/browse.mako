<%inherit file="/main.mako"/>
<%!
from app.utils.misc import formatcurrency
%>
<h1>Konti</h1>
<p>
    <a href=${escattr(urlfor("account.create_form"))}>Klik her for at oprette en konto</a>
</p>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Saldo</th>
        </tr>
    </thead>
    <tbody>
%for id, name, balance in accounts:
%if balance < 0:
    <tr style="background:#F88;">
%else:
    <tr style="background:#8F8;">
%endif
%if len(name) == 0:
        <td><a href=${escattr(urlfor("account.edit", id=id))}>[Tomt Navn]</td>
%else:
        <td><a href=${escattr(urlfor("account.edit", id=id))}>${escape(name)}</td>
%endif
            <td style="text-align:right;">${escape(formatcurrency(balance))}</td>
        </tr>
%endfor
    </tbody>
</table>
