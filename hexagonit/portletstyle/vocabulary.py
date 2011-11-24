# -*- coding: utf-8 -*-
"""Vocabulary of styles."""

from hexagonit.portletstyle import PortletStyleMessageFactory as _
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


class StylesVocabulary(object):
    """Vocabulary factory of portlet styles read from control panel registry."""
    implements(IVocabularyFactory)

    def __call__(self, context):
        registry = getUtility(IRegistry)
        styles = registry['hexagonit.portletstyle.interfaces.IPortletStyles.portlet_styles']

        # always have the default "no style" option available
        terms = [SimpleTerm(title=_(u"No style"), value="")]

        # add styles from the control panel
        for style in styles:
            try:
                value, title = style.split('|')
            except ValueError:
                continue

            terms.append(SimpleTerm(
                    title=title.strip(),
                    value=value.strip(),
                ))

        return SimpleVocabulary(terms)


StylesVocabularyFactory = StylesVocabulary()
