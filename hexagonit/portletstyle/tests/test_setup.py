# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.tests.base import IntegrationTestCase

import unittest2 as unittest


class TestSetup(IntegrationTestCase):
    """Test installation of hexagonit.portletstyle into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')

    def test_product_installed(self):
        """Test if hexagonit.portletstyle is installed with
        portal_quickinstaller.
        """
        self.failUnless(self.installer.isProductInstalled('hexagonit.portletstyle'))

    def test_uninstall(self):
        """Test if hexagonit.portletstyle is cleanly uninstalled."""
        self.installer.uninstallProducts(['hexagonit.portletstyle'])
        self.failIf(self.installer.isProductInstalled('hexagonit.portletstyle'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IPortletStyleLayer is registered."""
        from hexagonit.portletstyle.interfaces import IPortletStyleLayer
        from plone.browserlayer import utils
        self.failUnless(IPortletStyleLayer in utils.registered_layers())

    # cssregistry.xml
    def test_css_registered(self):
        """Test if portletstyle.s css file is registered with portal_css."""
        resources = self.portal.portal_css.getResources()
        ids = [r.getId() for r in resources]
        self.failUnless('++resource++portletstyle.css' in ids, 'portletstyle.css not found in portal_css')


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
