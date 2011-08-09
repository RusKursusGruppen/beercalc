<%inherit file="/main.mako"/>
<%!
    from app.utils.currency import formatcurrency
%><%
    self.breadcrumbs = (
        (urlfor("usage.new_form"), u"Ny afregning"),
    )
    product_ids = ",".join(escattr(id) for id, name, fixedprice in products)
    account_ids = ",".join(escattr(id) for id, name in accounts)
%>
<h1>Ny afregning</h1>
%if len(accounts) != 0 and len(products) != 0:
<% counter = 1 %>
<script type="text/javascript">
var preview_url = "${urlfor("usage.preview")}";
var product_ids = new Array(${product_ids});
var account_ids = new Array(${account_ids});
</script>
<script type="text/javascript" src="/static/javascript/usage.js"></script>

<section id="error">
    <h2>Fejl:</h2>
    <ul></ul>
</section>

<form id="usage_form" action=${escattr(urlfor("usage.new_form_do"))} method="post">
    <h2>Varebeholdning</h2>
    <table>
        <thead>
            <tr>
                <th>Produktnavn:</th>
                <th>Beholdning:</th>
                <th>Profit:</th>
                <th>Pris:</th>
                <th>
                    <a href=${escattr(urlfor("help.faq")+"#vejlederpris")}>
                        Vejlederpris:
                    </a>
                </th>
            </tr>
        </thead>
        <tbody>
%for id, name, fixedprice in products:
            <tr>
                <td>${escape(name)}:</td>
                <td><input type="text" class="stock" name=${escattr("stock_" + id)} style="width:4em" tabindex="${str(counter)}" value="" /></td>
<% counter += 1 %>
                <td><input type="text" class="profit" name=${escattr("profit_" + id)} style="width:4em" tabindex="${str(counter)}" value="0"/></td>
<% counter += 1 %>
                <td class="money" id=${escattr("price_" + id)}></td>
                <td class="money">${escape(formatcurrency(fixedprice))}</td>
            </tr>
%endfor
        </tbody>
    </table>

    <h2>Streger</h2>
    <table>
        <thead>
            <tr>
                <th>Konto:</th>
%for id, name, fixedprice in products:
                <th>${escape(name)}:</th>
%endfor
                <th>Forhåndsvisning:</th>
            </tr>
        </thead>
        <tbody>
%for aid, aname in accounts:
            <tr>
                <td><a href=${escattr(urlfor("account.edit", id=aid))}>${escape(aname)}</a></td>
%for pid, pname, fixedprice in products:
                <td><input type="text" class="usage" name="usage_${escape(aid)}_${escape(pid)}" value="0" style="width:4em" tabindex=${escattr(str(counter))} /></td>
<% counter += 1 %>
%endfor
                <td class="money" id=${escattr("preview_" + aid)}></td>
            </tr>

%endfor
        </tbody>
        <tfoot>
            <tr class="summary">
                <td>Total:</td>
%for id, name, fixedprice in products:
                <td id=${escattr("total_"+id)}>0</td>
%endfor
                <td class="money" id="preview_total">${escape(formatcurrency(0))}</td>
            </tr>
        </tfoot>
    </table>

    <input type="submit" name="submit" value="Afregn" tabindex=${escattr(str(counter))} />
</form>
%else:
    <p><strong>Fejl:</strong> Du har ikke angivet nogle 
%if len(products) == 0:
    <a href=${escattr(urlfor("product.browse"))}>produkter</a>
%if len(accounts) == 0:
    eller
%endif
%endif
%if len(accounts) == 0:
    <a href=${escattr(urlfor("account.browse"))}>konti</a>
%endif
endnu.</p>
%endif
