<%inherit file="/html5.mako"/>
<%!
    navbar_links = (
        ("account.browse", u"Konti"),
    )
%>
<head>
    <title>${escape(repr(endpoint))}</title>
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
</head>
<body>
<div id="header">RKG - Ølregnskab</div>
<div id="page" class="yui3-g">

<div class="yui3-u-1-5">
    <ul>
%for target, text in navbar_links:
        <li><a href=${escattr(urlfor(target))}>${escape(text)}</a></li>
%endfor
    </ul>
</div>
<div class="yui3-u-4-5">
    ${next.body()}
</div>
</body>
