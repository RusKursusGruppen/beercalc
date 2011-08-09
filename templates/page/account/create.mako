<%inherit file="/main.mako"/>
<%!
    from app.utils.misc import urlfor
%>
<%
    self.breadcrumbs = (
        (urlfor("account.browse"), u"Konti"),
        (urlfor("account.create_form"), u"Ny konto"),
    )
%>
<h1>Opret konto</h1>

<form action=${escattr(urlfor("account.create_do"))} method="post">
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
            <td><label for="istutor">Fritaget for at betale svind</label></td>
            <td><input type="checkbox" name="istutor" value="istutor" id="istutor"/>
        </tr>
        <tr>
            <td colspan="2" style="text-align:right;"><input type="submit" value="Opret konto"/>
        </tr>
    </table>
</form>
