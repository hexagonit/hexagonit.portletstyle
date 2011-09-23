from zope.i18nmessageid import MessageFactory

HexagonitPortletclassMessageFactory = MessageFactory('hexagonit.portletclass')

#: Default value for portlet CSS classes vocabulary.
DEFAULT_CLASSES = ['class1', 'class2', 'class3']


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
