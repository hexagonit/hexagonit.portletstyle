from hexagonit.portletclass import HexagonitPortletclassMessageFactory as _
from zope.interface import Interface
from zope.schema import TextLine


class IPortletClassSettings(Interface):
    """Configuration for portlet CSS class."""

    portlet_classes = TextLine(
        title=_(u'label_portlet_classes', default=u'Available portlet classes'),
        description=_(u'description_portlet_classes',
            default=u'Enter portlet CSS classes that users will be able to '
                    u'choose form the dropdown menu when editing portlets. '
                    u'One class per line. '),
        default='aaa')
