<%inherit file="/main.mako"/>
<%!
import pprint
%>

<h1>1 2 3 test</h1>

<table>
    <th><a href=${escattr("Hej")}>Navn</th>
</table>
<pre>
${escape(pprint.pformat(test))}
</pre>
