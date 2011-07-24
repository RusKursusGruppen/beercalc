<%inherit file="/main.mako"/>
<%!
from app.utils.misc import formatcurrency
%>
<h1>Konti</h1>

<h3>Debitorer</h3>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Skylder</th>
        </tr>
    </thead>
    <tbody>
%for id, name, balance in debtors:
        <tr>
            <td><a href=${escattr(url_for("account.edit", id=id))}>${escape(name)}</td>
            <td>${escape(formatcurrency(balance))}</td>
        </tr>
%endfor
    </tbody>
</table>

<h3>Kreditorer</h3>
<table>
    <thead>
        <tr>
            <th>Navn</th>
            <th>Har til gode</th>
        </tr>
    </thead>
    <tbody>
%for id, name, balance in creditors:
        <tr>
            <td><a href=${escattr(url_for("account.edit", id=id))}>${escape(name)}</td>
            <td>${escape(formatcurrency(balance))}</td>
        </tr>
%endfor
    </tbody>
</table>

