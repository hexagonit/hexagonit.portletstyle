# -*- coding: utf-8 -*-
"""Unit and integration tests for StylesVocabulary."""

from hexagonit.portletstyle.tests.base import IntegrationTestCase
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

import unittest2 as unittest


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
