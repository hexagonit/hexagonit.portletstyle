# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from hexagonit.portletclass.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName

import unittest2 as unittest


class TestCase(IntegrationTestCase):
    """Test installation of hexagonit.portletclass into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if hexagonit.portletclass is installed with
        portal_quickinstaller.
        """
        self.failUnless(self.installer.isProductInstalled('hexagonit.portletclass'))

    def test_uninstall(self):
        """Test if hexagonit.portletclass is cleanly uninstalled."""
        self.installer.uninstallProducts(['hexagonit.portletclass'])
        self.failIf(self.installer.isProductInstalled('hexagonit.portletclass'))


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
