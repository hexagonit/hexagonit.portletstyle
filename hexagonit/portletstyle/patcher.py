from plone.app.portlets.portlets import base
from plone.app.portlets.portlets import events
from plone.app.portlets.portlets import navigation
from plone.app.portlets.portlets import news
from plone.app.portlets.portlets import recent


def get_portlet_style(self):
    return self.data.portlet_style


def base_assignment__init__(self, *args, **kwargs):
    self.portlet_style = kwargs.get('portlet_style', u'')


# portlet.Events
def events_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))


def events_create(self, data):
    return events.Assignment(count=data.get('count', 5), state=data.get('state', ('published', )), portlet_style=data.get('portlet_style', u''))


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
    return navigation.Assignment(
        name=data.get('name', u""),
        root=data.get('root', u""),
        currentFolderOnly=data.get('currentFolderOnly', False),
        includeTop=data.get('includeTop', False),
        topLevel=data.get('topLevel', 0),
        bottomLevel=data.get('bottomLevel', 0),
        portlet_style=data.get('portlet_style', u'')
    )


# portlet.News
def news_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))


def news_create(self, data):
    return news.Assignment(count=data.get('count', 5), state=data.get('state', ('published', )), portlet_style=data.get('portlet_style', u''))


# portlet.Recent
def recent_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)


def recent_create(self, data):
    return recent.Assignment(count=data.get('count', 5), portlet_style=data.get('portlet_style', u''))
