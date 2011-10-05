from hexagonit.portletstyle import PortletStyleMessageFactory as _
from zope.interface import Interface
from zope import schema


class IPortletStyleLayer(Interface):
    """Marker interface for defining a Zope 3 browser layer."""


class IPortletStyles(Interface):
    """Configuration for portlet CSS class."""

    portlet_styles = schema.List(
        title=_(u'label_portlet_styles', default=u'Available portlet styles'),
        description=_(u'description_portlet_styles',
            default=u'Enter portlet styles that users will be able to '
                    u'choose form the dropdown menu when editing portlets. '
                    u'One class per line. '),
        value_type=schema.ASCIILine(),
        required=False,
    )