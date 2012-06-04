# -*- coding: utf-8 -*-
"""Module where all interfaces and schemas live."""

from hexagonit.portletstyle import PortletStyleMessageFactory as _
from hexagonit.portletstyle import styles_formatting
from zope.interface import Interface
from zope.schema import ASCIILine
from zope.schema import Choice
from zope.schema import List


class IPortletStyleLayer(Interface):
    """Marker interface for defining a Zope 3 browser layer."""


class IPortletStyles(Interface):
    """Control panel configuration of available portlet styles."""

    portlet_styles = List(
        title=_(u'label_portlet_styles', default=u'Available portlet styles'),
        description=_(u'description_portlet_styles',
            default=u'Enter portlet styles that users will be able to '
                    u'choose from the dropdown menu when editing portlets. '
                    u'One style per line. '),
        value_type=ASCIILine(),
        required=False,
        constraint=styles_formatting,
    )


class IPortletStyleDataProvider(Interface):
    portlet_style = Choice(
        title=_(u"Portlet style"),
        description=_(u"Select this portlet's style"),
        vocabulary=u"hexagonit.portletstyle.StylesVocabulary",
        required=True,
        default=" ",  # This makes the 'Default style' selected by default
    )
