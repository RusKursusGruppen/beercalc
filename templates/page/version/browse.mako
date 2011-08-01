<%!
import app.utils.date as dateutils
%>
<%inherit file="/main.mako"/>

<h1>Ældre versioner</h1>

<table>
    <thead>
        <tr>
            <th>Filnavn:</th>
            <th>Tidspunkt:</th>
            <th>Kommentar:</th>
    </thead>
    <tbody>
%for filename, date, comment in files:
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    date_str = escattr(date.strftime("%Y-%m-%dT%H:%M:%S"))
%>
        <tr>
            <td><a href=${escattr(urlfor("version.view", filename=filename))}>${escape(filename)}</a></td>
            <td><time datetime=${date_str} title=${date_str}>${date_delta}</time></td>
            <td>${escape(comment)}</td>
        </tr>
%endfor
    </tbody>
</table>
