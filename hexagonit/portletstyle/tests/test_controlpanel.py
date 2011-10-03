# -*- coding: utf-8 -*-
"""Unit and integration tests for Portlet Style Settings control panel
configlet.
"""

from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.interfaces import IPortletStyleSettings
from hexagonit.portletstyle.tests.base import IntegrationTestCase
from plone.app.testing import logout
from zope.component import getMultiAdapter
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

import unittest2 as unittest


class TestSettings(IntegrationTestCase):
    """Integration tests for Portlet Style Settings control panel configlet."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_portletstyle_controlpanel_view_accessible(self):
        """Test if the portletstyle control panel view is accessable."""
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="portletstyle-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_portletstyle_controlpanel_view_protected(self):
        """Test that the portletstyle control panel view is protected and
        anonymous users can't view or edit the portletstyle control panel.
        """
        logout()
        self.assertRaises(
            Unauthorized,
            self.portal.restrictedTraverse,
            '@@portletstyle-settings'
        )

    def test_akismet_in_controlpanel(self):
        """Check that there is an portletstyle entry in the control panel."""
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless('portletstyle' in [a.getAction(self)['id']
                            for a in self.controlpanel.listActions()])

    def test_record_portlet_styles(self):
        """Test that the portlet_styles record is in the control panel."""
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IPortletStyleSettings)
        self.assertEquals(settings.portlet_styles, u"")
        self.failUnless('portlet_styles' in IPortletStyleSettings)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
