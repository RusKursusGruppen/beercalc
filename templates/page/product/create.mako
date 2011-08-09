<%inherit file="/main.mako"/>
<h1>Nyt produkt</h1>
<%
    self.breadcrumbs = (
        (urlfor("product.browse"), u"Produkter"),
        (urlfor("product.create_form"), u"Tilføj"),
    )
%>

<form method="post" action=${escattr(urlfor("product.create_do"))}>
    <table>
        <tr>
            <td><label for="name">Navn:</label></td>
            <td><input type="text" name="name" id="name" />
        </tr>
        <tr>
            <td>
                <a href=${escattr(urlfor("help.faq")+"#vejlederpris")}>
                    Vejlederpris:
                </a>
            </td>
            <td><input type="text" name="fixedprice" id="fixedprice" />
        </tr>
    </table>
    <p>Vejlederprisen udregnes automatisk hvis den udelades.</p>
    <input type="submit" name="submit" value="Gem" />
</form>
