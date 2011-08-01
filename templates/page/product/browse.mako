<%!
from app.utils.currency import formatcurrency
%>
<%inherit file="/main.mako"/>
<h1>Produkter</h1>

<nav>
    <ul>
        <li><a href=${escattr(urlfor("product.create_form"))}>Nyt produkt</a></li>
    </ul>
</nav>

<table>
    <thead>
        <tr>
            <th>Navn:</th>
            <th>Samlet udgift:</th>
            <th>Vejlederpris:</th>
        </tr>
    </thead>
    <tbody>
%for id, name, total_purchase, fixedprice, real_fixedprice in products:
        <tr>
            <td><a href=${escattr(urlfor("product.edit", product_id=id))}>${escape(name)}</td>
            <td class="money">${escape(formatcurrency(total_purchase))}</td>
%if fixedprice is None:
            <td class="money dynamic" title="Dynamisk">${escape(formatcurrency(real_fixedprice))}</td>
%else:
            <td class="money">${escape(formatcurrency(fixedprice))}</td>
%endif
            <td><a href=${escattr(urlfor("product.delete", product_id=id))}>[Slet]</a></td>
        </tr>
%endfor
    </tbody>
</table>
