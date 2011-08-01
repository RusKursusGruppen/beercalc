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
    tz = date.strftime("%z")
    datetime = escattr(date.strftime("%Y-%m-%dT%H:%M:%S") + "+%s:%s" % (tz[1:3], tz[-2:]))
    date_str = escattr(date.strftime("%Y-%m-%d %H:%M:%S"))
%>
        <tr>
            <td><a href=${escattr(urlfor("version.view", filename=filename))}>${escape(filename)}</a></td>
            <td><time datetime=${datetime} title=${date_str}>${date_delta}</time></td>
            <td>${escape(comment)}</td>
        </tr>
%endfor
    </tbody>
</table>
