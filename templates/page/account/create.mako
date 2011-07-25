<%inherit file="/main.mako"/>
<h1>Opret konto</h1>

<form action="" method="post">
<table>
    <tr>
        <td><label for="name">Navn</label></td>
        <td><input type="text" name="name" id="name"/>
    </tr>
    <tr>
        <td><label for="email">E-mail</label></td>
        <td><input type="text" name="email" id="email"/>
    </tr>
    <tr>
        <td><label for="istutor">Er rusvejleder</label></td>
        <td><input type="checkbox" name="istutor" value="istutor" id="istutor"/>
    </tr>
    <tr>
        <td colspan="2" style="text-align:right;"><input type="submit" value="Opret konto"/>
    </tr>
</table>
