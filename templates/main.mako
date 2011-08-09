<%inherit file="/html5.mako"/>
<%!
    header = u"<!-- " + u"Daniel Egeberg Bjørn Uhre Arnholtz "*1000 + u"-->"
    navbar_links = (
        ("index.index", u"Forside/status", "home"),
        ("usage.new_form", u"Ny afregning", "usage"),
        ("product.browse", u"Produkter", "products"),
        ("account.browse", u"Konti", "accounts"),
        ("misc.cashlog", u"Kasse", "cash"),
        ("version.browse", u"Ældre versioner", "versions"),
        ("misc.transfer", u"Import/Eksport", "import"),
    )
%>
<%
    content = capture(next.body)
%>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Ølregnskab - ${escape(widget.doc_title())}</title>
    <link rel="stylesheet" href="/static/css/yui.css" type="text/css" />
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <link rel="icon" href="/static/beer.ico" type="image/x-icon" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
    <script type="text/javascript" src="/static/javascript/utils.js"></script>
</head>
<body>
<header id="header">Ølregnskab - ${escape(widget.doc_title())}</header>
<div id="page" class="yui3-g">

<nav class="yui3-u-1-5" id="nav_container">
    <ul id="nav">
%for target, text, id in navbar_links:
        <li id=${escattr("nav_"+id)}><a href=${escattr(urlfor(target))}>${escape(text)}</a></li>
%endfor
    </ul>
</nav>

<div class="yui3-u-4-5" id="content_container">
<nav class="yui3-u-1" id="breadcrumbs">
%for n, (url, title) in enumerate(((urlfor("index.index"), u"Forside"),) + next.breadcrumbs):
%if n > 0:
→
%endif
    <a href=${escattr(url)}>${escape(title)}</a>
%endfor
</nav>
<section id="content">
    ${content}
</section>
</div>
</div>
</body>
${header}
