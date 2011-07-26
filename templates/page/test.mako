<%inherit file="/main.mako"/>
<%
    from pprint import pformat
%>
<pre>
    ${escape(pformat(test))}
</pre>
