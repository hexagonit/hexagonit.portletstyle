# -*- coding: utf-8 -*-
"""Unit and integration tests for StylesVocabulary."""

from hexagonit.portletstyle.tests.base import IntegrationTestCase
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import mock
import unittest2 as unittest

styles = 'hexagonit.portletstyle.interfaces.IPortletStyles.portlet_styles'


class TestVocabularyUnit(unittest.TestCase):
    """Light-weight unit tests for how values from control panel get parsed."""

    def _get_terms(self, context=None):
        """Prepare an instance of StylesVocabulary and return it's terms."""
        from hexagonit.portletstyle.vocabulary import StylesVocabulary
        return list(StylesVocabulary()(context))

    def _prepare_logger(self, level='WARN'):
        """Set a certain logging level and add a handler that can be used
        for inspecting what was written to log."""
        from StringIO import StringIO
        import logging

        log = StringIO()
        logger = logging.getLogger('hexagonit.portletstyle')
        logger.addHandler(logging.StreamHandler(log))
        logger.setLevel(logging.WARN)
        return log

    @mock.patch('hexagonit.portletstyle.vocabulary.getUtility')
    def test_empty(self, utility):
        """Test that we have the 'default style' vocabulary item available even
        if there are no styles saved in control panel."""
        utility.return_value = {styles: []}
        terms = self._get_terms()

        # only the "default style" term is here, which is injected
        # as the first item
        self.assertEquals(1, len(terms))
        self.assertEquals("Default style", terms[0].title)

    @mock.patch('hexagonit.portletstyle.vocabulary.getUtility')
    def test_filter_invalid_delimiters(self, utility):
        """Test that invalid delimiters don't break the vocabulary but rather
        simply get filtered out.
        """
        log = self._prepare_logger()

        utility.return_value = {styles: [
            'no_delimiter',
            'valid delimiter|Valid delimiter',
            'too|much|delimiters',
        ]}
        terms = self._get_terms()

        # Apart from the "default style" term, we should have one more term
        # for one valid line in styles specified above; other lines get filtered
        self.assertEquals(2, len(terms))
        self.assertEquals("Default style", terms[0].title)
        self.assertEquals("Valid delimiter", terms[1].title)

        # Two styles get skipped and there should be a warning in logger
        # for both
        log.seek(0)
        entries = log.readlines()
        self.assertEquals(entries[0], "Filtered out a style because it cannot be parsed: 'no_delimiter'\n")
        self.assertEquals(entries[1], "Filtered out a style because it cannot be parsed: 'too|much|delimiters'\n")

    @mock.patch('hexagonit.portletstyle.vocabulary.getUtility')
    def test_ignore_empty_lines(self, utility):
        """Test that empty lines are simply ignored."""
        log = self._prepare_logger()

        utility.return_value = {styles: [
            '',
            ' ',
            '        ',
        ]}
        terms = self._get_terms()

        # Only the default 'Default style' style should be in terms
        self.assertEquals(1, len(terms))
        self.assertEquals("Default style", terms[0].title)

        # Empty lines are ignored without any log entries.
        log.seek(0)
        entries = log.readlines()
        self.assertEquals(0, len(entries))

    @mock.patch('hexagonit.portletstyle.vocabulary.getUtility')
    def test_append_style_from_portlet(self, utility):
        """If a portlet has a style assigned that is no longer listed in
        portlet_styles, than we need to add it to the drop-down menu, so it's
        still possible to select it.
        """

        portlet = mock.Mock(spec='portlet_style'.split())
        portlet.portlet_style = 'bar'

        utility.return_value = {styles: ['foo|Foo']}
        terms = self._get_terms(portlet)

        # 'Default style' + 'Foo' from the list + 'bar' from the portlet
        self.assertEquals(3, len(terms))
        self.assertEquals("Default style", terms[0].title)
        self.assertEquals("Foo", terms[1].title)
        self.assertEquals("bar", terms[2].title)


class TestVocabularyIntegration(IntegrationTestCase):
    """Integration tests for StylesVocabulary vocabulary that reads values
    from control panel configlet.
    """

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_vocabulary_reads_from_control_panel(self):
        """Integration test to check if styles are correctly read from the
        control panel configlet and transformed into vocabulary items."""
        vocabularyFactory = getUtility(
            IVocabularyFactory,
            name=u"hexagonit.portletstyle.StylesVocabulary"
        )

        vocabulary = vocabularyFactory(self.portal)
        terms = list(vocabulary)

        # "default style" + 3 default styles from registry.xml
        self.assertEquals(4, len(terms))

        # are default styles from registry.xml here?
        self.assertEquals('No header', terms[1].title)
        self.assertEquals('noheader', terms[1].value)
        self.assertEquals('No footer', terms[2].title)
        self.assertEquals('nofooter', terms[2].value)
        self.assertEquals('No header and no footer', terms[3].title)
        self.assertEquals('noheader nofooter', terms[3].value)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
