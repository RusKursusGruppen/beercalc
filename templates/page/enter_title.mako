<%inherit file="/html5.mako" />
<head>
    <title>Velkommen til beercalc</title>
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
    <link rel="icon" href="/static/beer.ico" type="image/x-icon" />
    <script type="text/javascript" src="/static/javascript/jquery.js"></script>
</head>
<body>
<head>
    <title>Indtast titel på regnskabet</title>
</head>
<body id="enter_title">
<form action=${escattr(urlfor("misc.enter_title_do"))} method="post" id="enter_title_form">
    <h1>Indtast navn</h1>
    <p>
        Velkommen til beercalc. Inden du kan komme videre skal du lige give
        dit regnskab et navn. Det kunne f.eks. være <em>Rushold 1 - 2011</em>.
    </p>
    <p><label for="title"><strong>Regnskabets navn:</strong></label>
    <input type="text" name="title" id="title" />
    <input type="submit" value="Gå til beercalc" />
</form>
</body>
