from plone.app.portlets.portlets.base import Assignment
from plone.portlets import interfaces  # import IPortletDataProvider as old
from zope import schema
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface


PortletStyleMessageFactory = MessageFactory('hexagonit.portletstyle')
Assignment.css_class = -1


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


class IPortletDataProvider(Interface):
    css_class = schema.TextLine(title=u'CSS class',
                                description=u'CSS class description',
                                required=True,
                                default=u'')
interfaces.IPortletDataProvider = IPortletDataProvider
