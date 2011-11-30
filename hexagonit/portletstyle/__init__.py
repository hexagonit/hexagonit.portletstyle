# -*- coding: utf-8 -*-
"""Init and utils."""

from Acquisition import aq_inner
from plone.app.portlets import cache
from plone.app.portlets.cache import get_language
from plone.app.portlets.portlets.base import Assignment
from plone.portlets import interfaces
from Products.CMFCore.utils import getToolByName
from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope.interface import Invalid
from zope.schema import Choice

import re

_ = PortletStyleMessageFactory = MessageFactory('hexagonit.portletstyle')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

# This is needed so that old portlets can be edited
Assignment.portlet_style = u' '


# Patch IPortletDataProvider so it has an additional field
class IPortletDataProvider(Interface):
    portlet_style = Choice(
        title=_(u"Portlet style"),
        description=_(u"Select this portlet's style"),
        vocabulary=u"hexagonit.portletstyle.StylesVocabulary",
        required=True,
        default=" ",  # This makes the 'Default style' selected by default
    )
interfaces.IPortletDataProvider = IPortletDataProvider


# Patch render_cachekey so it also takes into account the selected style
def new_render_cachekey(fun, self):
    context = aq_inner(self.context)

    def add(brain):
        path = brain.getPath().decode('ascii', 'replace')
        return "%s\n%s\n\n" % (path, brain.modified)
    fingerprint = "".join(map(add, self._data()))

    anonymous = getToolByName(context, 'portal_membership').isAnonymousUser()
    return "".join((
        getToolByName(aq_inner(self.context), 'portal_url')(),
        get_language(aq_inner(self.context), self.request),
        str(anonymous),
        self.manager.__name__,
        self.data.__name__,
        self.data.portlet_style or "",
        fingerprint))
cache.render_cachekey = new_render_cachekey


# Styles formatting validator for control panel config
class NotAValidCssClassError(Exception):
    """An exception thrown when a style does not have a valid CSS class."""


class EmptyLineError(Exception):
    """An exception thrown when a line is empty or contains only whitespace."""


def styles_formatting(styles):
    """Iterate over all styles and check that they can be sucessfully parsed.
    Ignore empty lines.

    :param styles: List of pipe-delimited styles in "ccs|title" format.
    :type styles: list

    :rtype: boolean
    :return: True if all styles are correcty formatted

    >>> from hexagonit.portletstyle import styles_formatting

    Test formatting of a list of valid styles
    >>> styles_formatting(['foo|faz', 'bar|baz'])
    True

    Test empty line is ignored
    >>> styles_formatting(['foo|bar', '  '])
    True

    Test non-valid CSS class error
    >>> styles_formatting(['2foo|bar'])
    Traceback (most recent call last):
    ...
    Invalid: Style 1 does not have a valid CSS class: 2foo|bar

    Test some other error
    >>> styles_formatting(['title_is_empty|'])
    Traceback (most recent call last):
    ...
    Invalid: Style 1 is not correctly formatted: title_is_empty|
    """
    for index, style in enumerate(styles):
        try:
            parse_style(style)
        except EmptyLineError:
            continue
        except NotAValidCssClassError:
            raise Invalid("Style %i does not have a valid CSS class: %s" % (index + 1, style))
        except:
            raise Invalid("Style %i is not correctly formatted: %s" % (index + 1, style))
    return True


def parse_style(style):
    """Parse pipe-delimited style into a css part and a title part.

    :param style: Pipe-delimited style in "ccs|title" format.
    :type style: string

    :rtype: tuple of strings
    :return: A pair of strings representing css class for a style and it's title

    >>> from hexagonit.portletstyle import parse_style

    Test parsing a valid style
    >>> parse_style('foo|bar')
    ('foo', 'bar')

    Test parsing a valid style with multiple CSS classes
    >>> parse_style('foo bar baz|Multistyle')
    ('foo bar baz', 'Multistyle')

    Test an empty style
    >>> parse_style(' ')
    Traceback (most recent call last):
    ...
    EmptyLineError

    Test an empty title
    >>> parse_style('foo|')
    Traceback (most recent call last):
    ...
    Exception

    Test an empty CSS class
    >>> parse_style('|foo')
    Traceback (most recent call last):
    ...
    NotAValidCssClassError

    Test an invalid CSS classes
    >>> parse_style('2nd|foo')
    Traceback (most recent call last):
    ...
    NotAValidCssClassError
    """
    # ignore empty lines
    if not style.strip():
        raise EmptyLineError()

    css, title = style.split("|")
    css.strip()
    title.strip()

    # Check for empty title part
    if not title:
        raise Exception()

    # Check for empty CSS class part
    if not css:
        raise NotAValidCssClassError()

    # Check for CSS class validity; a style can have multiple CSS classes
    # so we first need to split them
    for cls in css.split():
        if not _is_valid_css_class(cls):
            raise NotAValidCssClassError()

    return css, title


def _is_valid_css_class(string):
    """Check if string is a valid CSS class.
    http://stackoverflow.com/questions/448981/what-characters-are-valid-in-css-class-names

    :param string: String to check for validity.
    :type string: string

    :rtype: boolean
    :return: True if string is a valid CSS class, False otherwise

    >>> from hexagonit.portletstyle import _is_valid_css_class

    Valid classes
    >>> _is_valid_css_class('foo')
    True
    >>> _is_valid_css_class('-single-dash')
    True
    >>> _is_valid_css_class('_underscore')
    True
    >>> _is_valid_css_class('numbered123')
    True

    Invalid classes
    >>> _is_valid_css_class('x')
    False
    >>> _is_valid_css_class('--double-dash')
    False
    >>> _is_valid_css_class('123leading-numbers')
    False
    """
    exp = re.compile('^-?[_a-zA-Z][_a-zA-Z0-9-]+$')
    if exp.match(string):
        return True
    return False
