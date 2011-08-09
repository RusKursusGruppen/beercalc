<%!
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
            <td>
                <label for="fixedprice">
                    <a href=${escattr(urlfor("help.faq")+"#vejlederpris")}>
                        Vejlederpris:
                    </a>
                </label>
            </td>
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
        <tr>
            <td>${escape(pname)}</td>
            <td class="money">${escape(formatcurrency(price))}</td>
            <td>${str(quantity)}</td>
            <td>${widget.timedelta(date)}</td>
            <td><a href=${escattr(urlfor("product.purchase_delete", purchase_id = purchase_id, product_id = id))}>[Slet]</a>
        </tr>
%endfor
    </tbody>
</table>

<p><a href=${escattr(urlfor("product.purchase", product_id=id))}>Nyt indkøb</a></p>
