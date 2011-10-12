from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


class StylesVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        registry = getUtility(IRegistry)
        styles = registry['hexagonit.portletstyle.interfaces.IPortletStyles.portlet_styles']
        return SimpleVocabulary.fromValues(styles)

StylesVocabularyFactory = StylesVocabulary()