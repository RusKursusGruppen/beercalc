<%inherit file="/main.mako"/>

<h1>Kontoimport</h1>

<form method="post" action=${escattr(urlfor("account.import_do"))}>
    <textarea name="data" style="width: 100%; height: 40em"></textarea>
    <input type="submit" name="submit" value="Importer" />
</form>
