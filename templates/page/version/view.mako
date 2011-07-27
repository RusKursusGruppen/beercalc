<%!
import app.utils.date as dateutils
%>
<%inherit file="/main.mako"/>
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    date_str = escattr(date.strftime("%d/%m-%Y %H:%M:%S"))
%>

<h1>Version: ${escape(filename)}</h2>

<dl>
    <dt>Filnavn:</dt>
    <dd>${escape(filename)}</dd>

    <dt>Tidspunkt:</dt>
    <dd title=${date_str}>${date_delta}</dd>

    <dt>Kommentar:</dt>
    <dd>${escape(comment)}</dd>
</dl>

%if filename != "save.beer":
<p><a href=${escattr(urlfor("version.rollback", filename=filename))}>Rul tilbage til denne version.</a></p>
%endif
