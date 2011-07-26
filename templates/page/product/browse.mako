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
            <th>Samlet udgift:</th>
            <th>Vejlederpris:</th>
        </tr>
    </thead>
    <tbody>
%for id, name, total_purchase, fixedprice in products:
        <tr>
            <td><a href=${escattr(urlfor("product.edit", product_id=id))}>${escape(name)}</td>
            <td style="text-align:right;">${escape(formatcurrency(total_purchase))}</td>
%if fixedprice is None:
            <td style="font-style:italic">Dynamisk</td>
%else:
            <td>${escape(formatcurrency(fixedprice))}</td>
%endif
            <td><a href=${escattr(urlfor("product.delete", product_id=id))}>[Slet]</a></td>
        </tr>
%endfor
    </tbody>
</table>
