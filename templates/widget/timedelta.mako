<%!
    import app.utils.date as dateutils
%><%
    date_delta = escape(dateutils.formatdelta(date-dateutils.now()))
    tz = date.strftime("%z")
    datetime = escattr(date.strftime("%Y-%m-%dT%H:%M:%S") + "+%s:%s" % (tz[1:3], tz[-2:]))
    date_str = escattr(date.strftime("%Y-%m-%d %H:%M:%S"))
%><time datetime=${datetime} title=${date_str}>${date_delta}</time>
