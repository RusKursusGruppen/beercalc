<%!
import app.utils.date as dateutils
from app.utils.currency import formatcurrency, formatnumber
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
                <input name="fixedprice" id="fixedprice" value=${escattr(formatnumber(fixedprice))} />
%endif
            </td>
        </tr>
    </table>
    <p>Vejlederprisen udregnes automatisk hvis den udelades.</p>
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
            <th></th>
        </tr>
    </thead>
    <tbody>
%for pname, price, quantity, date, purchase_id in purchases:
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    tz = date.strftime("%z")
    datetime = escattr(date.strftime("%Y-%m-%dT%H:%M:%S") + "+%s:%s" % (tz[1:3], tz[-2:]))
    date_str = escattr(date.strftime("%Y-%m-%d %H:%M:%S"))
%>
        <tr>
            <td>${escape(pname)}</td>
            <td class="money">${escape(formatcurrency(price))}</td>
            <td>${str(quantity)}</td>
            <td><time datetime=${datetime} title=${date_str}>${date_delta}</time></td>
            <td><a href=${escattr(urlfor("product.purchase_delete", purchase_id = purchase_id, product_id = id))}>[Slet]</a>
        </tr>
%endfor
    </tbody>
</table>

<p><a href=${escattr(urlfor("product.purchase", product_id=id))}>Nyt indkøb</a></p>
