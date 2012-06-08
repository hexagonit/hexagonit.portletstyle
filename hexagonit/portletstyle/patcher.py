# -*- coding: utf-8 -*-
"""Monkey patches to support choosing a style for a portlet."""
from collective.quickupload.portlet import quickuploadportlet
from hexagonit.portletstyle.interfaces import IPortletStyleDataProvider
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget
from plone.app.portlets.portlets import base
from plone.app.portlets.portlets import events
from plone.app.portlets.portlets import navigation
from plone.app.portlets.portlets import news
from plone.app.portlets.portlets import recent
from plone.app.portlets.portlets import rss
from plone.app.portlets.portlets import search
from plone.portlet.collection import collection
from plone.portlet.static import static
from qi.portlet.TagClouds import tagcloudportlet
from zope.formlib import form
from zope.formlib.form import Widgets
from zope.formlib.form import _createWidget
from zope.formlib.form import canWrite
from zope.formlib.form import expandPrefix
from zope.formlib.interfaces import DISPLAY_UNWRITEABLE
from zope.formlib.interfaces import IDisplayWidget
from zope.formlib.interfaces import IInputWidget
from zope.interface import directlyProvides


def get_portlet_style(self):
    return self.data.portlet_style


def base_assignment__init__(self, *args, **kwargs):
    self.portlet_style = kwargs.get('portlet_style', u' ')


# portlet.Events
class INewEventsPortlet(events.IEventsPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Events portlet."""


def events_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewEventsPortlet)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))


def events_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewEventsPortlet)
    super(events.AddForm, self).__init__(context, request)


def events_create(self, data):
    return events.Assignment(**data)


def events_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewEventsPortlet)
    super(events.EditForm, self).__init__(context, request)


# portlet.Navigation
class INewNavigationPortlet(navigation.INavigationPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Navigation portlet."""


def navigation_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, )
    self.name = kwargs.get('name', u"")
    self.root = kwargs.get('root', None)
    self.currentFolderOnly = kwargs.get('currentFolderOnly', False)
    self.includeTop = kwargs.get('includeTop', False)
    self.topLevel = kwargs.get('topLevel', 1)
    self.bottomLevel = kwargs.get('bottomLevel', 0)


def navigation_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewNavigationPortlet)
    super(navigation.AddForm, self).__init__(context, request)


def navigation_create(self, data):
    return navigation.Assignment(**data)


def navigation_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewNavigationPortlet)
    super(navigation.EditForm, self).__init__(context, request)


# portlet.News
class INewNewsPortlet(news.INewsPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for News portlet."""


def news_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewNewsPortlet)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))


def news_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewNewsPortlet)
    super(news.AddForm, self).__init__(context, request)


def news_create(self, data):
    return news.Assignment(**data)


def news_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewNewsPortlet)
    super(news.EditForm, self).__init__(context, request)


# portlet.Recent
class INewRecentPortlet(recent.IRecentPortlet, IPortletStyleDataProvider):
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
class INewRSSPortlet(rss.IRSSPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for RSS portlet."""


def rss_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewRSSPortlet)
    self.portlet_title = kwargs.get('portlet_title', u'')
    self.count = kwargs.get('count', 5)
    self.url = kwargs.get('url', u'')
    self.timeout = kwargs.get('timeout', 100)


def rss_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewRSSPortlet)
    super(rss.AddForm, self).__init__(context, request)


def rss_create(self, data):
    return rss.Assignment(**data)


def rss_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewRSSPortlet)
    super(rss.EditForm, self).__init__(context, request)


# portlet.Search
class INewSearchPortlet(search.ISearchPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Search portlet."""


def search_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewSearchPortlet)
    self.enableLivesearch = kwargs.get('enableLivesearch', u'')


def search_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewSearchPortlet)
    super(search.AddForm, self).__init__(context, request)


def search_create(self, data):
    return search.Assignment(**data)


def search_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewSearchPortlet)
    super(search.EditForm, self).__init__(context, request)


# portlet.Static
class INewStaticPortlet(static.IStaticPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Static portlet."""


def static_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.header = kwargs.get('header', u"")
    self.text = kwargs.get('text', u"")
    self.omit_border = kwargs.get('omit_border', False)
    self.footer = kwargs.get('footer', u"")
    self.more_url = kwargs.get('more_url', u"")


def static_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewStaticPortlet)
    self.form_fields['text'].custom_widget = static.WYSIWYGWidget
    super(static.AddForm, self).__init__(context, request)


def static_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewStaticPortlet)
    self.form_fields['text'].custom_widget = static.WYSIWYGWidget
    super(static.EditForm, self).__init__(context, request)


# portlet.Collection
class INewCollectionPortlet(collection.ICollectionPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Collection portlet."""


def collection_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewCollectionPortlet)
    self.header = kwargs.get('header', u"")
    self.target_collection = kwargs.get('target_collection', None)
    self.limit = kwargs.get('limit', None)
    self.random = kwargs.get('random', None)
    self.show_more = kwargs.get('show_more', True)
    self.show_dates = kwargs.get('show_dates', False)


def collection_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewCollectionPortlet)
    super(collection.AddForm, self).__init__(context, request)


def collection_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewCollectionPortlet)
    super(collection.EditForm, self).__init__(context, request)


# portlet.quickupload
class INewQuickUploadPortlet(quickuploadportlet.IQuickUploadPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Quick Upload portlet."""


def portlet_quickupload_assignment__init__(self, portlet_style="", header="", upload_portal_type="auto", upload_media_type=""):
    directlyProvides(self, INewQuickUploadPortlet)
    self.portlet_style = portlet_style
    self.header = header
    self.upload_portal_type = upload_portal_type
    self.upload_media_type = upload_media_type


def quickuploadportlet_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewQuickUploadPortlet)
    super(quickuploadportlet.AddForm, self).__init__(context, request)


def quickuploadportlet_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewQuickUploadPortlet)
    super(quickuploadportlet.EditForm, self).__init__(context, request)


# qi.portlet.TagClouds
class INewTagCloudPortlet(tagcloudportlet.ITagCloudPortlet, IPortletStyleDataProvider):
    """DataProvider Interface for Tag Cloud portlet."""


def portlet_TagClouds_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    directlyProvides(self, INewTagCloudPortlet)
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


def tagcloudportlet_addform__init__(self, context, request):
    self.form_fields = form.Fields(INewTagCloudPortlet)
    self.form_fields['root'].custom_widget = UberSelectionWidget
    super(tagcloudportlet.AddForm, self).__init__(context, request)


def tagcloudportlet_editform__init__(self, context, request):
    self.form_fields = form.Fields(INewTagCloudPortlet)
    self.form_fields['root'].custom_widget = UberSelectionWidget
    super(tagcloudportlet.EditForm, self).__init__(context, request)


def setUpEditWidgets(form_fields, form_prefix, context, request,
                     adapters=None, for_display=False,
                     ignore_request=False):
    if adapters is None:
        adapters = {}

    widgets = []
    for form_field in form_fields:
        field = form_field.field
        # Adapt context, if necessary
        interface = form_field.interface
        adapter = adapters.get(interface)
        if adapter is None:
            if interface is None:
                adapter = context
            else:
                adapter = interface(context, context)  # Work around.
            adapters[interface] = adapter
            if interface is not None:
                adapters[interface.__name__] = adapter

        field = field.bind(adapter)

        readonly = form_field.for_display
        readonly = readonly or (field.readonly and not form_field.for_input)
        readonly = readonly or (
            (form_field.render_context & DISPLAY_UNWRITEABLE)
            and not canWrite(adapter, field)
            )
        readonly = readonly or for_display

        if readonly:
            iface = IDisplayWidget
        else:
            iface = IInputWidget
        widget = _createWidget(form_field, field, request, iface)

        prefix = form_prefix
        if form_field.prefix:
            prefix = expandPrefix(prefix) + form_field.prefix

        widget.setPrefix(prefix)

        if ignore_request or readonly or not widget.hasInput():
            # Get the value to render
            value = field.get(adapter)
            widget.setRenderedValue(value)

        widgets.append((not readonly, widget))

    return Widgets(widgets, prefix=form_prefix)
