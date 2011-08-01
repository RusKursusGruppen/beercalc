<%!
import app.utils.date as dateutils
%>
<%inherit file="/main.mako"/>
<%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    tz = date.strftime("%z")
    datetime = escattr(date.strftime("%Y-%m-%dT%H:%M:%S") + "+%s:%s" % (tz[1:3], tz[-2:]))
    date_str = escattr(date.strftime("%Y-%m-%d %H:%M:%S"))
%>

<h1>Version: ${escape(filename)}</h1>

<dl>
    <dt>Filnavn:</dt>
    <dd>${escape(filename)}</dd>

    <dt>Tidspunkt:</dt>
    <dd><time datetime=${datetime} title=${date_str}>${date_delta}</time></dd>

    <dt>Kommentar:</dt>
    <dd>${escape(comment)}</dd>
</dl>

<nav>
    <h2>Handlinger</h2>

    <ul>
        <li><a href=${escattr(urlfor("version.export", filename=filename))}>Eksportér</a></li>
    %if filename != "save.beer":
        <li><a href=${escattr(urlfor("version.rollback", filename=filename))}>Gendan.</a></li>
    %endif
    </ul>
</nav>
