<%inherit file="/main.mako"/>
<h1>Ny optælling</h1>
%if len(accounts) != 0 and len(products) != 0:
<% counter = 1 %>
<script type="text/javascript">
var preview_url = "${urlfor("usage.preview")}";
</script>
<script type="text/javascript" src="/static/javascript/usage.js"></script>

<form id="usage_form" action=${escattr(urlfor("usage.new_form_do"))} method="post">
    <h2>Varebeholdning</h2>
    <p style="display:none;color:red;" id="stock_error"></p>
    <table>
        <thead>
            <tr>
                <th>Produktnavn:</th>
                <th>Beholdning:</th>
                <th>Profit:</th>
            </tr>
        </thead>
        <tbody>
%for id, name in products:
            <tr>
                <td>${escape(name)}:</td>
                <td><input type="text" class="stock" name=${escattr("stock_" + id)} style="width:4em" tabindex="${str(counter)}" value="" /></td>
<% counter += 1 %>
                <td><input type="text" name=${escattr("profit_" + id)} style="width:4em" tabindex="${str(counter)}" value="0"/></td>
<% counter += 1 %>
            </tr>
%endfor
        </tbody>
    </table>

    <h2>Streger</h2>
    <table>
        <thead>
            <tr>
                <th>Konto:</th>
%for id, name in products:
                <th>${escape(name)}:</th>
%endfor
                <th>Forhåndsvisning:</th>
            </tr>
        </thead>
        <tbody>
%for aid, aname in accounts:
            <tr>
                <td><a href=${escattr(urlfor("account.edit", id=aid))}>${escape(aname)}</a></td>
%for pid, pname in products:
                <td><input type="text" name="usage_${escape(aid)}_${escape(pid)}" value="0" style="width:4em" tabindex=${escattr(str(counter))} /></td>
<% counter += 1 %>
%endfor
                <td id=${escattr("preview_" + aid)}></td>
            </tr>

%endfor
        </tbody>
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
