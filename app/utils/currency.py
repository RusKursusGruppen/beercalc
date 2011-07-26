# -*- coding: utf-8 -*-

def parsenumber(text):
        text = text.strip()
        negative = False
        if text[0] == "-":
            text = text[1:]
            negative = True

        if not all(x in "0123456789,." for x in text):
            return
        text = "".join(text.split("."))
        text = (text + "00").split(",")
        if len(text) > 2:
            return
        number = int("".join(text[0:1]) + "".join(text[1:2])[0:2])

        if negative:
            return -number
        return number

def formatcurrency(integer):
    prefix = u""
    if integer < 0:
        integer = abs(integer)
        prefix = u"-"

    fraction = unicode(integer % 100)
    integer = unicode(integer // 100)

    # Add thousands seperator
    integer = integer[::-1]
    integer = u".".join(integer[i:i+3] for i in range(0, len(integer), 3))
    integer = integer[::-1]
    
    # Zero pad 
    fraction = (u"0" + fraction)[-2:]
    
    return prefix + integer + u"," + fraction + u" kr."
