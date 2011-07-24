<%inherit file="/main.mako"/>
<%!
import pprint
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
            <td>${balance} kr.</td>
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
            <td>${balance} kr.</td>
        </tr>
%endfor
    </tbody>
</table>

