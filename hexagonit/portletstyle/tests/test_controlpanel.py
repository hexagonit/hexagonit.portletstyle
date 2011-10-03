# -*- coding: utf-8 -*-
"""Unit and integration tests for Portlet Style Settings control panel
configlet.
"""

from hexagonit.portletstyle.tests.base import IntegrationTestCase
from zope.component import getMultiAdapter

import unittest2 as unittest


class TestSettings(IntegrationTestCase):
    """Integration tests for Portlet Style Settings control panel configlet."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_portletstyle_controlpanel_accessible(self):
        """Test if the portletstyle control panel view is accessable."""
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="portletstyle-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
