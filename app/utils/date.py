# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone

local = timezone("Europe/Copenhagen")
utc = timezone("UTC")

def now():
    return datetime.utcnow().replace(tzinfo = utc)

def nowtuple():
    return totuple(now())

def totuple(t):
    t = t.astimezone(utc)
    return t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond

def fromtuple(tuple_):
    return datetime(*tuple_, tzinfo = utc).astimezone(local)
