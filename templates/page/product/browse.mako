<%!
from app.utils.currency import formatcurrency
%>
<%inherit file="/main.mako"/>
<h1>Produkter</h1>

<p>
    <a href=${escattr(urlfor("product.create_form"))}>Nyt produkt</a>
</p>

<table>
    <thead>
        <tr>
            <th>Navn:</th>
            <th>Beholdning:</th>
            <th>Vejlederpris:</th>
        </tr>
    </thead>
    <tbody>
%for id, name, stock, fixedprice in products:
        <tr>
            <td><a href=${escattr(urlfor("product.edit", product_id=id))}>${escape(name)}</td>
            <td style="text-align:right;">${escape(str(stock))}</td>
%if fixedprice is None:
            <td style="font-style:italic">Dynamisk</td>
%else:
            <td>${escape(formatcurrency(fixedprice))}</td>
%endif
        </tr>
%endfor
    </tbody>
</table>
