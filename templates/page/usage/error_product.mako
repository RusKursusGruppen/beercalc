<%inherit file="/main.mako" />
<h1>Ny optælling</h1>
<p>
    <strong>Fejl:</strong> Du har ikke angivet
    <a href=${escattr(urlfor("product.create_form"))}>nogle produkter</a>
    endnu.
</p>
