<%inherit file="/html5.mako"/>
<%!
    header = u"<!-- " + u"Daniel Egeberg Bjørn Uhre Arnholtz "*1000 + u"-->"
    navbar_links = (
        ("index.index", u"Forside/status"),
        ("usage.new_form", u"Ny afregning"),
        ("product.browse", u"Produkter"),
        ("account.browse", u"Konti"),
        ("misc.cashlog", u"Kasse"),
        ("version.browse", u"Ældre versioner"),
        ("misc.transfer", u"Import/Eksport"),
    )
%>
<head>
    <title>Ølregnskab - ${escape(widget.doc_title())}</title>
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <link rel="icon" href="/static/beer.ico" type="image/x-icon" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
</head>
<body>
<div id="header">Ølregnskab - ${escape(widget.doc_title())}</div>
<div id="page" class="yui3-g">

<div class="yui3-u-1-5" id="nav_container">
    <ul id="nav">
%for target, text in navbar_links:
        <li><a href=${escattr(urlfor(target))}>${escape(text)}</a></li>
%endfor
    </ul>
</div>
<div class="yui3-u-4-5" id="content_container">
<div id="content">
    ${next.body()}
</div>
</div>
</div>
</body>
${header}
