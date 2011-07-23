<%
    response.headers["Content-Type"] = "text/html; charset=UTF-8"
%><!DOCTYPE html>
<html>
${next.body()}
</html>
