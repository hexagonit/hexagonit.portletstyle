from plone.app.portlets.portlets import base
from plone.app.portlets.portlets import events
from plone.app.portlets.portlets import recent


def get_portlet_style(self):
    return self.data.portlet_style


def base_assignment__init__(self, *args, **kwargs):
    self.portlet_style = kwargs.get('portlet_style', '')


# portlet.Recent
def recent_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)
def recent_create(self, data):
    return recent.Assignment(count=data.get('count', 5), portlet_style=data.get('portlet_style', ''))


# portlet.Events
def events_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', 5)
    self.state = kwargs.get('state', ('published', ))
def events_create(self, data):
    return events.Assignment(count=data.get('count', 5), state=data.get('state', ('published', )), portlet_style=data.get('portlet_style', ''))