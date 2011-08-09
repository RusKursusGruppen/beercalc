<%!
from app.utils.currency import formatcurrency, formatnumber
%>
<%
    self.breadcrumbs = (
        (urlfor("product.browse"), u"Produkter"),
        (urlfor("product.edit", product_id=product_id), product_name),
        (urlfor("product.purchase", product_id=product_id), u"Tilføj Indkøb"),
    )
%>
<%inherit file="/main.mako"/>

<h1>Nyt indkøb til '${escape(product_name)}'</h1>

<form method="post" action=${escattr(urlfor("product.purchase_do", product_id=product_id))}>
    <table>
        <tr>
            <td><label for="name">Navn:</label></td>
            <td><input type="text" name="name" id="name" /></td>
        </tr>
        <tr>
            <td><label for="price">Pris:</label></td>
            <td><input type="text" name="price" id="price" /></td>
        </tr>
        <tr>
            <td><label for="quantity">Antal:</label></td>
            <td><input type="text" name="quantity" id="quantity" /></td>
        </tr>
    </table>

    <input type="submit" name="submit" value="Tilføj indkøb" />
</form>
