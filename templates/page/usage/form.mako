<%
    counter = 1
%>
<%inherit file="/main.mako"/>

<h1>Ny optælling</h1>

<form action=${escattr(urlfor("usage.new_form_do"))} method="post">
    <h2>Varebeholdning</h2>
    <table>
        <thead>
            <tr>
                <th>Produktnavn:</th>
                <th>Beholdning:</th>
            </tr>
        </thead>
        <tbody>
%for id, name in products:
            <tr>
                <td>${escape(name)}:</td>
                <td><input type="text" name="stock_${escape(id)}" style="width:4em" tabindex=${escattr(str(counter))}/></td>
            </tr>
<%
    counter += 1
%>
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
            </tr>
        </thead>
        <tbody>
%for aid, aname in accounts:
            <tr>
                <td><a href=${escattr(urlfor("account.edit", id=aid))}>${escape(aname)}</a></td>
%for pid, pname in products:
                <td><input type="text" name="usage_${escape(aid)}_${escape(pid)}" style="width:4em" tabindex=${escattr(str(counter))} /></td>
<%
    counter += 1
%>
%endfor
            </tr>

%endfor
        </tbody>
    </table>

    <input type="submit" name="submit" value="Afregn" tabindex=${escattr(str(counter))} />
</form>
