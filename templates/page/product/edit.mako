<%!
import app.utils.date as dateutils
from app.utils.currency import formatcurrency
%>
<%inherit file="/main.mako"/>
<h1>Produkt: ${escape(name)}</h1>

<form method="post" action=${escattr(urlfor("product.edit_do", product_id=id))}>
    <table>
        <tr>
            <td><label for="name">Navn:</label></td>
            <td><input name="name" id="name" value=${escattr(name)} /></td>
        </tr>
        <tr>
            <td><label for="fixedprice">Vejlederpris:</label></td>
            <td>
%if fixedprice is None:
                <input name="fixedprice" id="fixedprice" />
%else:
                <input name="fixedprice" id="fixedprice" value=${escattr(str(fixedprice))} />
%endif
            </td>
        </tr>
    </table>
    <input type="submit" name="submit" value="Gem" />
</form>

<h2>Indkøb</h2>

<table>
    <thead>
        <tr>
            <th>Navn:</th>
            <th>Pris:</th>
            <th>Antal:</th>
            <th>Dato:</th>
        </tr>
    </thead>
    <tbody>
%for pname, price, quantity, date in purchases:
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    date_str = escattr(date.strftime("%d/%m-%Y %H:%M:%S"))
%>
        <tr>
            <td>${escape(pname)}</td>
            <td>${escape(formatcurrency(price))}</td>
            <td>${str(quantity)}</td>
            <td title=${date_str}>${date_delta}</td>
        </tr>
%endfor
    </tbody>
</table>

<p><a href="">Nyt indkøb</a></p>
