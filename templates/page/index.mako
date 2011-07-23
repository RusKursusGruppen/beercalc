<%inherit file="/main.mako" />
<h1>
    RUS-Browser
</h1>
<p>
%if page > 0:
    <a href="${url_for("rus.browse", page=page-1)}">Forrige side</a>
%else:
    Forrige side
%endif
%if page < pagecount - 1:
    | <a href="${url_for("rus.browse", page=page+1)}">Næste side</a>
%else:
    | Næste side
%endif
</p>
<p>
%for x in range(pagecount):
%if x == page:
    [${unicode(x)}]
%else:
    <a href="${url_for("rus.browse", page=x)}">[${unicode(x)}]</a>
%endif
%endfor
</p>
<form action="" method="post">
<table>
    <thead>
        <tr>
            <th><input type="checkbox"/></th>
            <th>Årgang</th>
            <th>Rustur</th>
            <th>Navn</th>
            <th>Telefon</th>
            <th>E-mail</th>
        </tr>
    </thead>
    <tbody>
%for (id, name, phone, email, year, rustur) in russer:
        <tr>
            <td>
                <input type="checkbox" />
            </td>
            <td>
                ${escape(year or "")}
            </td>
            <td>
                ${escape(rustur or "")}
            </td>
            <td>
                <a href="${url_for("rus.edit", id=id)}">${escape(name or "")}
            </td>
            <td>
                ${escape(phone or "")}
            </td>
            <td>
%if email:
                <a href=${esc_attr("mailto:" + email)}>${escape(email)}</a>
%endif
            </td>
        </tr>
%endfor
    </tbody>
</table>
</form>
