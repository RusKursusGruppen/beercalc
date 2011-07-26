<%inherit file="/html5.mako"/>
<%!
    navbar_links = (
        ("account.browse", u"Konti"),
        ("usage.new_form", u"Ny afregning"),
        ("product.browse", u"Produkter"),
    )
%>
<head>
    <title>${escape(repr(endpoint))}</title>
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
</head>
<body>
<div id="header">${escape(repr(endpoint))}</div>
<div id="page" class="yui3-g">

<div class="yui3-u-1-5" id="nav_container">
    <ul id="nav">
%for target, text in navbar_links:
        <li><a href=${escattr(urlfor(target))}>${escape(text)}</a></li>
%endfor
    </ul>
</div>
<div class="yui3-u-4-5">
<div id="content">
    ${next.body()}
</div>
</div>
</body>
