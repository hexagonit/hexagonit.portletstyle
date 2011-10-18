# -*- coding: utf-8 -*-
"""Init and utils."""

from plone.app.portlets.portlets.base import Assignment
from plone.portlets import interfaces
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema import Choice


PortletStyleMessageFactory = MessageFactory('hexagonit.portletstyle')
Assignment.portlet_style = -1


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


class IPortletDataProvider(Interface):
    portlet_style = Choice(
        title=u"Portlet style",
        description=u"Select this portlet's' style",
        vocabulary=u"hexagonit.portletstyle.StylesVocabulary",
        required=False,
    )
interfaces.IPortletDataProvider = IPortletDataProvider
