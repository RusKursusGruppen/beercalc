<%inherit file="/main.mako"/>
<%!
from app.utils.currency import formatcurrency
%>
<h1>Konti</h1>
<nav>
    <ul>
        <li><a href=${escattr(urlfor("account.create_form"))}>Ny konto</a></li>
        <li><a href=${escattr(urlfor("account.import"))}>Importer konti</a></li>
    </ul>
</nav>
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
        <tr class="balance_negative">
%else:
        <tr class="balance_positive">
%endif
%if len(name) == 0:
            <td><a href=${escattr(urlfor("account.edit", id=id))}>[Tomt Navn]</a></td>
%else:
            <td><a href=${escattr(urlfor("account.edit", id=id))}>${escape(name)}</a></td>
%endif
            <td class="money">${escape(formatcurrency(balance))}</td>
        </tr>
%endfor
    </tbody>
</table>
