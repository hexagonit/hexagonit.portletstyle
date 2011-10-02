from hexagonit.portletstyle import PortletStyleMessageFactory as _
from zope.interface import Interface
from zope.schema import TextLine

class IPortletStyleLayer(Interface):
    """Marker interface for defining a Zope 3 browser layer."""

# 
# class IPortletStyleSettings(Interface):
#     """Configuration for portlet CSS class."""
# 
#     portlet_classes = TextLine(
#         title=_(u'label_portlet_classes', default=u'Available portlet classes'),
#         description=_(u'description_portlet_classes',
#             default=u'Enter portlet CSS classes that users will be able to '
#                     u'choose form the dropdown menu when editing portlets. '
#                     u'One class per line. '),
#         default='aaa')
