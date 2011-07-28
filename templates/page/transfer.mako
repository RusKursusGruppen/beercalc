<%inherit file="/main.mako" />
<h1>Import/Eksport</h1>
<h3>Eksportér</h3>
<p>
    <a href=${escattr(urlfor("misc.export_file"))}>Download</a>
</p>
<h3>Importér</h3>
<form action=${escattr(urlfor("misc.import_file"))} method="post" enctype="multipart/form-data">
    <label for="savefile">Vælg fil der skal importeres:</label><br/>
    <input id="savefile" type="file" name="savefile" />
    <br/>
    <br/>
    <input type="submit" value="Importér"/>
</form>
