def get_css_class(self):
    return self.data.css_class


def base_assignment__init__(self, *args, **kwargs):
    self.css_class = kwargs.get('css_class', '')


from plone.app.portlets.portlets import base
def recent_assignment__init__(self, *args, **kwargs):
    base.Assignment.__init__(self, *args, **kwargs)
    self.count = kwargs.get('count', '')


def recent_create(self, data):
    return base.Assignment(count=data.get('count', ''), css_class=data.get('css_class', ''))
