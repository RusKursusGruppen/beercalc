<%inherit file="/html5.mako"/>
<head>
    <title>${escape(repr(endpoint))}</title>
</head>
<body>
    ${next.body()}
</body>
