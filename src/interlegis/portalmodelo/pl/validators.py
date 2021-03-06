# -*- coding: utf-8 -*-

from datetime import date
from DateTime import DateTime
from datetime import datetime
from zope.interface import Invalid
from zope.i18nmessageid import MessageFactory

_ = MessageFactory("interlegis.portalmodelo.pl")


def check_birthday(value):
    now = datetime.now().date()
    if isinstance(value, DateTime):
        value = value.asdatetime()

    if isinstance(value, datetime):
        value = value.date()

    if not isinstance(value, date):
        raise ValueError

    # Is in the past?
    delta = (now - value)
    if not delta.days > 0:
        raise Invalid(_(u'Birthday must be a date in the past.'))
    else:
        return True
