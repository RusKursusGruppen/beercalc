<%inherit file="/main.mako"/>

<h1>Kontoimport</h1>
<p>
    Der må i tekstboksen nedenunder indsættes en konti per linje. Per linje
    må indsættets navn + email. Hvilken rækkefølge det indsættes i er
    lige meget. Det finder <em>beercalc</em> selv ud af. Den piller blot
    e-mail adressen ud, og antager at resten er kontoens navn.
</p>
<p>
    Husk at du altid kan rulle tilbage til en tidligere version hvis du
    ikke er tilfreds med resultatet.
</p>
<form method="post" action=${escattr(urlfor("account.import_do"))}>
    <textarea name="data" style="width: 100%; height: 40em"></textarea>
    <input type="submit" name="submit" value="Importer" />
</form>
