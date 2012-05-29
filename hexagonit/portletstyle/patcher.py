# -*- coding: utf-8 -*-
"""Monkey patches to support choosing a style for a portlet."""

from Products.PloneGazette.portlet import subscribe
from plone.app.portlets.portlets import base
from plone.app.portlets.portlets import events
from plone.app.portlets.portlets import navigation
from plone.app.portlets.portlets import news
from plone.app.portlets.portlets import recent
from plone.app.portlets.portlets import rss
from plone.app.portlets.portlets import search


from zope.component import queryUtility
from zope.schema.interfaces import IVocabularyFactory

from hexagonit.portletstyle import _
from zope.interface import Interface
from zope.interface import implements
from zope.schema import Choice
from plone.app.portlets.portlets.recent import IRecentPortlet
from zope.formlib import form
from zope.interface import directlyProvides


# Patch IPortletDataProvider so it has an additional field
class IPortletDataProvider(Interface):
    portlet_style = Choice(
        title=_(u"Portlet style"),
        description=_(u"Select this portlet's style"),
        vocabulary=u"hexagonit.portletstyle.StylesVocabulary",
        required=True,
        default=" ",  # This makes the 'Default style' selected by default
    )
# interfaces.IPortletDataProvider = IPortletDataProvider


def get_portlet_style(self):
    return self.data.portlet_style


def base_assignment__init__(self, *args, **kwargs):
    # if queryUtility(IVocabularyFactory, name=u'hexagonit.portletstyle.StylesVocabulary'):
    #     import pdb; pdb.set_trace()
        self.portlet_style = kwargs.get('portlet_style', u' ')


# portlet.Events
def events_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))


def events_create(self, data):
    return events.Assignment(**data)


# portlet.Navigation
def navigation_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.name = kwargs.get('name', u"")
    self.root = kwargs.get('root', None)
    self.currentFolderOnly = kwargs.get('currentFolderOnly', False)
    self.includeTop = kwargs.get('includeTop', False)
    self.topLevel = kwargs.get('topLevel', 1)
    self.bottomLevel = kwargs.get('bottomLevel', 0)


def navigation_create(self, data):
    return navigation.Assignment(**data)


# portlet.News
def news_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))


def news_create(self, data):
    return news.Assignment(**data)


# portlet.Recent
class INewRecentPortlet(recent.IRecentPortlet, IPortletDataProvider):
    """DataProvider Interface for Recent portlet."""


def recent_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewRecentPortlet)
    self.count = kwargs.get('count', 5)


def recent_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewRecentPortlet)
    super(recent.AddForm, self).__init__(context, request)


def recent_create(self, data):
    return recent.Assignment(**data)


def recent_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewRecentPortlet)
    super(recent.EditForm, self).__init__(context, request)


# portlet.Rss
def rss_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.portlet_title = kwargs.get('portlet_title', u'')
    self.count = kwargs.get('count', 5)
    self.url = kwargs.get('url', u'')
    self.timeout = kwargs.get('timeout', 100)


def rss_create(self, data):
    return rss.Assignment(**data)


# portlet.Search
def search_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.enableLivesearch = kwargs.get('enableLivesearch', u'')


def search_create(self, data):
    return search.Assignment(**data)


# portlet.Static
def static_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.header = kwargs.get('header', u"")
    self.text = kwargs.get('text', u"")
    self.omit_border = kwargs.get('omit_border', False)
    self.footer = kwargs.get('footer', u"")
    self.more_url = kwargs.get('more_url', u"")


# portlet.Collection
def collection_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.header = kwargs.get('header', u"")
    self.target_collection = kwargs.get('target_collection', None)
    self.limit = kwargs.get('limit', None)
    self.random = kwargs.get('random', None)
    self.show_more = kwargs.get('show_more', True)
    self.show_dates = kwargs.get('show_dates', False)


# portlet.quickupload
def portlet_quickupload_assignment__init__(self, portlet_style="", header="", upload_portal_type="auto", upload_media_type=""):
    self.portlet_style = portlet_style
    self.header = header
    self.upload_portal_type = upload_portal_type
    self.upload_media_type = upload_media_type


# qi.portlet.TagClouds
def portlet_TagClouds_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.header = kwargs.get('header', u"")
    self.portletTitle = kwargs.get('portletTitle', 'TagCloud')
    self.levels = kwargs.get('levels', 5)
    self.count = kwargs.get('count', 0)
    self.restrictSubjects = kwargs.get('restrictSubjects', [])
    self.filterSubjects = kwargs.get('filterSubjects', [])
    self.restrictTypes = kwargs.get('restrictTypes', [])
    self.wfStates = kwargs.get('wfStates', [])
    self.refreshInterval = kwargs.get('refreshInterval', 3600)
    self.root = kwargs.get('root', u'')


# portlets.SubscribeNewsletter
def portlet_SubscribeNewsletter_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.name = kwargs.get('name', u"")
    self.newsletters = kwargs.get('newsletters', None)







class IRecentPortlet(IPortletDataProvider, IRecentPortlet):
    """For overriding recent portlet Assignment class implements."""

class RecentAssignment(base.Assignment):

    implements(IRecentPortlet)

    def __init__(self, *args, **kwargs):
        base.Assignment.__init__(self, *args, **kwargs)
        self.count = kwargs.get('count', 5)

    @property
    def title(self):
        return _(u"Recent items")


# portlet_style = Choice(
#     title=_(u"Portlet style"),
#     description=_(u"Select this portlet's style"),
#     vocabulary=u"hexagonit.portletstyle.StylesVocabulary",
#     required=True,
#     default=" ",  # This makes the 'Default style' selected by default
# )



class RecentAddForm(base.AddForm):
    form_fields = form.Fields(IRecentPortlet)
    label = _(u"Add Recent Portlet")
    description = _(u"This portlet displays recently modified content.")

    def create(self, data):
        import pdb; pdb.set_trace()
        return Assignment(**data)


class RecentEditForm(base.EditForm):
    form_fields = form.Fields(IRecentPortlet)
    label = _(u"Edit Recent Portlet")
    description = _(u"This portlet displays recently modified content.")