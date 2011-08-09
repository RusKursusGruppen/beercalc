<%inherit file="/main.mako"/>
<%
    self.breadcrumbs = (
        (urlfor("version.browse"), u"Ældre versioner"),
        (urlfor("version.view", filename=filename), filename),
    )
%>
<h1>Version: ${escape(filename)}</h1>

<dl>
    <dt>Filnavn:</dt>
    <dd>${escape(filename)}</dd>

    <dt>Tidspunkt:</dt>
    <dd>${widget.timedelta(date)}</dd>

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
