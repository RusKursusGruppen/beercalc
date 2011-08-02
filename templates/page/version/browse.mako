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
        <tr>
            <td><a href=${escattr(urlfor("version.view", filename=filename))}>${escape(filename)}</a></td>
            <td>${widget.timedelta(date)}</td>
            <td>${escape(comment)}</td>
        </tr>
%endfor
    </tbody>
</table>
