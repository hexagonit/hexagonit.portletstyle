def get_portlet_style(self):
    return self.data.portlet_style


def base_assignment__init__(self, *args, **kwargs):
    self.portlet_style = kwargs.get('portlet_style', '')


from plone.app.portlets.portlets import base
def recent_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', '')


def recent_create(self, data):
    return base.Assignment(count=data.get('count', ''), portlet_style=data.get('portlet_style', ''))
