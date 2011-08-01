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
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Ølregnskab - ${escape(widget.doc_title())}</title>
    <link rel="stylesheet" href="/static/css/yui.css" type="text/css" />
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <link rel="icon" href="/static/beer.ico" type="image/x-icon" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
</head>
<body>
<header id="header">Ølregnskab - ${escape(widget.doc_title())}</header>
<div id="page" class="yui3-g">

<nav class="yui3-u-1-5" id="nav_container">
    <ul id="nav">
%for target, text in navbar_links:
        <li><a href=${escattr(urlfor(target))}>${escape(text)}</a></li>
%endfor
    </ul>
</nav>

<div class="yui3-u-4-5" id="content_container">
<section id="content">
    ${next.body()}
</section>
</div>
</div>
</body>
${header}
