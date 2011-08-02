function formatnumber(n) {
    n = n.toString();

    r = "";
    for (var i = 1; i < n.length; ++i) {
        r += n[n.length - i];
        if (i > 0 && i % 3 == 0 && i) {
            r += ".";
        }
    }
    r += n[0];

    return r.split("").reverse().join("");
}

function formatcurrency(n) {
    prefix = "";
    if (n < 0) {
        n = Math.abs(n);
        prefix = "-";
    }

    fraction = (n % 100).toString();
    if (fraction.length == 1) {
        fraction = "0" + fraction;
    }
    n = Math.floor(n / 100);

    return formatnumber(n) + "," + fraction + " kr.";
}

function validatenumber(s, allow_negative) {
    if (typeof allow_negative == "undefined" || allow_negative) {
        return /^-?\d(\.?\d)*(,\d{1,2})?$/.test(s);
    }
    else {
        return /^\d(\.?\d)*(,\d{1,2})?$/.test(s);
    }
}
