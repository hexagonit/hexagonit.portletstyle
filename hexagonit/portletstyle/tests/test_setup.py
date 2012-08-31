# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.tests.base import IntegrationTestCase


class TestSetup(IntegrationTestCase):
    """Test installation of hexagonit.portletstyle into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_product_installed(self):
        """Test if hexagonit.portletstyle is installed with
        portal_quickinstaller.
        """
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('hexagonit.portletstyle'))

    def test_collective_quickupload_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('collective.quickupload'))

    def test_qi_portlet_TagClouds_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('qi.portlet.TagClouds'))

    def test_browserlayer(self):
        """Test that IPortletStyleLayer is registered."""
        from hexagonit.portletstyle.interfaces import IPortletStyleLayer
        from plone.browserlayer import utils
        self.assertIn(IPortletStyleLayer, utils.registered_layers())

    def get_action(self, name):
        controlpanel = getToolByName(self.portal, 'portal_controlpanel')
        return controlpanel.getActionObject(name)

    def test_controlpanel__portletsytles__title(self):
        action = self.get_action('Products/portletstyles')
        self.assertEqual(action.title, u'Portlet Styles')

    def test_controlpanel__portletsytles__appId(self):
        action = self.get_action('Products/portletstyles')
        self.assertEqual(action.appId, 'hexagonit.portletstyle')

    def test_controlpanel__portletsytles__condition_expr(self):
        action = self.get_action('Products/portletstyles')
        self.assertEqual(action.condition, '')

    def test_controlpanel__portletsytles__url_expr(self):
        action = self.get_action('Products/portletstyles')
        self.assertEqual(action.getActionExpression(), 'string:${portal_url}/@@portletstyles')

    def test_controlpanel__portletsytles__visible(self):
        action = self.get_action('Products/portletstyles')
        self.assertTrue(action.visible)

    def test_controlpanel__portletsytles__permissions(self):
        action = self.get_action('Products/portletstyles')
        self.assertEqual(action.permissions, ('Manage portal',))

    def test_cssregistry(self):
        """Test if portletstyle.s css file is registered with portal_css."""
        resources = self.portal.portal_css.getResources()
        ids = [r.getId() for r in resources]
        self.assertIn('++resource++portletstyle.css', ids)

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile(
                'profile-hexagonit.portletstyle:default'), u'0102')

    def test_registry(self):
        from hexagonit.portletstyle.interfaces import IPortletStyles
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        records = getUtility(IRegistry).forInterface(IPortletStyles)
        self.assertEqual(records.portlet_styles, [
            'noheader|No header', 'nofooter|No footer', 'noheader nofooter|No header and no footer'])

    def test_uninstall(self):
        """Test if hexagonit.portletstyle is cleanly uninstalled."""
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['hexagonit.portletstyle'])
        self.failIf(installer.isProductInstalled('hexagonit.portletstyle'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['hexagonit.portletstyle'])
        from hexagonit.portletstyle.interfaces import IPortletStyleLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPortletStyleLayer, utils.registered_layers())

    def test_ininstall__controlpanel(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['hexagonit.portletstyle'])
        self.assertIsNone(self.get_action('Products/portletstyles'))

    def test_ininstall__cssregistry(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['hexagonit.portletstyle'])
        resources = self.portal.portal_css.getResources()
        ids = [r.getId() for r in resources]
        self.assertNotIn('++resource++portletstyle.css', ids)

    def test_ininstall__registry(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['hexagonit.portletstyle'])
        from hexagonit.portletstyle.interfaces import IPortletStyles
        from plone.registry.interfaces import IRegistry
        from zope.component import getUtility
        # remove="true" is not working as expected...
        records = getUtility(IRegistry).forInterface(IPortletStyles)
        self.assertEqual(records.portlet_styles, [
            'noheader|No header', 'nofooter|No footer', 'noheader nofooter|No header and no footer'])
