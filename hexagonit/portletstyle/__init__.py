# -*- coding: utf-8 -*-
"""Init and utils."""

from Acquisition import aq_inner
from plone.app.portlets import cache
from plone.app.portlets.cache import get_language
from plone.app.portlets.portlets.base import Assignment
from plone.portlets import interfaces
from Products.CMFCore.utils import getToolByName
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.schema import Choice

_ = PortletStyleMessageFactory = MessageFactory('hexagonit.portletstyle')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""

# This is needed so that old portlets can be edited
Assignment.portlet_style = -1

# Patch IPortletDataProvider so it has an additional field
class IPortletDataProvider(Interface):
    portlet_style = Choice(
        title=_(u"Portlet style"),
        description=_(u"Select this portlet's style"),
        vocabulary=u"hexagonit.portletstyle.StylesVocabulary",
        required=False,
    )
interfaces.IPortletDataProvider = IPortletDataProvider

# Patch render_cachekey so it also takes into account the selected style
def new_render_cachekey(fun, self):
    context = aq_inner(self.context)

    def add(brain):
        path = brain.getPath().decode('ascii', 'replace')
        return "%s\n%s\n\n" % (path, brain.modified)
    fingerprint = "".join(map(add, self._data()))

    anonymous = getToolByName(context, 'portal_membership').isAnonymousUser()
    return "".join((
        getToolByName(aq_inner(self.context), 'portal_url')(),
        get_language(aq_inner(self.context), self.request),
        str(anonymous),
        self.manager.__name__,
        self.data.__name__,
        self.data.portlet_style or "",
        fingerprint))
cache.render_cachekey = new_render_cachekey
