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
        </tr>
    </thead>
    <tbody>
%for id, name, stock in products:
        <tr>
            <td><a href=${escattr(urlfor("product.edit", product_id=id))}>${escape(name)}</td>
            <td style="text-align:right;">${escape(str(stock))}</td>
        </tr>
%endfor
    </tbody>
</table>
