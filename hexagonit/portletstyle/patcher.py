# -*- coding: utf-8 -*-
"""Monkey patches to support choosing a style for a portlet."""

from plone.app.portlets.portlets import base
from plone.app.portlets.portlets import events
from plone.app.portlets.portlets import navigation
from plone.app.portlets.portlets import news
from plone.app.portlets.portlets import recent
from plone.app.portlets.portlets import rss
from plone.app.portlets.portlets import search


def get_portlet_style(self):
    return self.data.portlet_style


def base_assignment__init__(self, *args, **kwargs):
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
def recent_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)


def recent_create(self, data):
    return recent.Assignment(**data)


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
