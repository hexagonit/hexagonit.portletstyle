from zope.i18nmessageid import MessageFactory

HexagonitPortletclassMessageFactory = MessageFactory('hexagonit.portletclass')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

from plone.app.portlets.portlets.base import Assignment
Assignment.css_class = -1


from zope import schema
from plone.portlets import interfaces # import IPortletDataProvider as old
from zope.interface import Interface
class IPortletDataProvider(Interface):
    css_class = schema.Int(title=u'CSS class id',
                            description=u'Css class description.',
                            required=True,
                            default=5)
interfaces.IPortletDataProvider = IPortletDataProvider