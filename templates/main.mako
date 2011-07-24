<%inherit file="/html5.mako"/>
<head>
    <title>${escape(repr(endpoint))}</title>
    <link rel="stylesheet" href="/static/css/main.css" type="text/css" />
</head>
<body>
    ${next.body()}
</body>
