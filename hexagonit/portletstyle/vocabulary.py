# -*- coding: utf-8 -*-
"""Vocabulary of styles."""

from hexagonit.portletstyle import PortletStyleMessageFactory as _
from hexagonit.portletstyle import parse_style
from hexagonit.portletstyle import EmptyLineError
from hexagonit.portletstyle import NotAValidCssClassError
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm


import logging

logger = logging.getLogger("hexagonit.portletstyle")


class StylesVocabulary(object):
    """Vocabulary factory of portlet styles read from control panel registry."""
    implements(IVocabularyFactory)

    def __call__(self, context):
        registry = getUtility(IRegistry)
        styles = registry['hexagonit.portletstyle.interfaces.IPortletStyles.portlet_styles']

        # always have the default "default style" option available
        terms = [SimpleTerm(title=_(u"Default style"), value=" ")]

        # add styles from the control panel, but filter out invalid ones
        for style in styles:

            try:
                css, title = parse_style(style)
            except EmptyLineError:
                continue
            except NotAValidCssClassError:
                logger.warn("Filtered out a style because it doesn't have a valid CSS class: '%s'" % style)
                continue
            except:
                logger.warn("Filtered out a style because it cannot be parsed: '%s'" % style)
                continue

            terms.append(SimpleTerm(
                    title=title,
                    value=css,
                ))

        return SimpleVocabulary(terms)


StylesVocabularyFactory = StylesVocabulary()
