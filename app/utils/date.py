# -*- coding: utf-8 -*-
from datetime import datetime
from pytz import timezone

local = timezone("Europe/Copenhagen")
utc = timezone("UTC")


def now():
    return datetime.utcnow().replace(tzinfo=utc)


def nowtuple():
    return totuple(now())


def totuple(t):
    t = t.astimezone(utc)
    return t.year, t.month, t.day, t.hour, t.minute, t.second, t.microsecond


def fromtuple(tuple_):
    return datetime(*tuple_, tzinfo=utc).astimezone(local)


def formatdelta(delta):
    """
        Danish pretty representation of time deltas
    """
    if abs(delta) != delta:  # Negative values are in the past
        prefix = u""
        postfix = u" siden"
        delta = abs(delta)
    else:
        prefix = u"Om "
        postfix = u""

    days = delta.days
    weeks = days // 7
    days = days % 7

    seconds = delta.seconds
    minutes = seconds // 60
    hours = minutes // 60
    minutes = minutes % 60
    seconds = seconds % 60

    for (noun, plural, var) in (
        (u"uge", u"uger", weeks),
        (u"dag", u"dage", days),
        (u"time", u"timer", hours),
        (u"minut", u"minutter", minutes),
        (u"sekund", u"sekunder", seconds),
        (u"mikrosekund", u"mikrosekunder", delta.microseconds),
    ):
        if var == 0:
            continue

        return prefix + unicode(var) + u" " + (noun if var == 1 else plural) + postfix
