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

    def _get_terms(self):
        """Prepare an instance of StylesVocabulary and return it's terms."""
        from hexagonit.portletstyle.vocabulary import StylesVocabulary
        return list(StylesVocabulary()(None))

    @mock.patch('zope.component.getUtility')
    def test_empty(self, utility):
        """Test that we have the 'no style' vocabulary item available even
        if there are no styles saved in control panel."""
        utility.return_value = {styles: []}
        terms = self._get_terms()

        # only the "no style" term is here, which is injected as the first item
        self.assertEquals(1, len(terms))
        self.assertEquals("No style", terms[0].title)

    @mock.patch('zope.component.getUtility')
    def test_filtering_invalid_delimiters(self, utility):
        """Test that invalid delimiters don't break the vocabulary but rather
        simply get filtered out.
        """
        utility.return_value = {styles: [
            'no_delimiter',
            'valid delimiter|Valid delimiter',
            'too|much|delimiters',
        ]}
        terms = self._get_terms()

        # apart from the "no style" term, we should have one more term
        # for one valid line in styles specified above; other lines get skipped
        self.assertEquals(2, len(terms))
        self.assertEquals("No style", terms[0].title)
        self.assertEquals("Valid delimiter", terms[1].title)


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

        # "no style" + 3 default styles from registry.xml
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
