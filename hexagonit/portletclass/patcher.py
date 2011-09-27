def get_css_class(self):
    return self.data.css_class

from zope import schema
css_class = schema.Int(title=u'CSS class id',
                description=u'Css class description.',
                required=True,
                default=5)
