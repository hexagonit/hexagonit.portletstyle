# -*- coding: utf-8 -*-
"""Upgrades step tests for this package."""

from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):
    """Test upgrade steps."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_upgrade_0100_to_0101(self):
        """Uninstall qi.portlet.TagClouds and see if upgrade step reinstall it.
        """
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['qi.portlet.TagClouds'])
        self.failIf(installer.isProductInstalled('qi.portlet.TagClouds'))
        from hexagonit.portletstyle.upgrades import upgrade_0100_to_0101
        upgrade_0100_to_0101(self.portal)
        self.failUnless(installer.isProductInstalled('qi.portlet.TagClouds'))
