# -*- coding: utf-8 -*-
"""Unit and integration tests for Portlet Styles control panel
configlet.
"""

from AccessControl import Unauthorized
from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.interfaces import IPortletStyles
from hexagonit.portletstyle.tests.base import IntegrationTestCase
from plone.app.testing import logout
from plone.registry.interfaces import IRegistry
from zope.component import getMultiAdapter
from zope.component import getUtility

import unittest2 as unittest


class TestControlPanel(IntegrationTestCase):
    """Integration tests for Portlet Styles control panel configlet."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']

    def test_portletstyle_controlpanel_view_accessible(self):
        """Test if the portletstyle control panel view is accessable."""
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name="portletstyles")
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
            '@@portletstyles'
        )

    def test_portlet_styles_in_controlpanel(self):
        """Check that there is an portletstyle entry in the control panel."""
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless('portletstyles' in [a.getAction(self)['id']
                            for a in self.controlpanel.listActions()])

    def test_record_portlet_styles(self):
        """Test that the portlet_styles record is in the control panel."""
        registry = getUtility(IRegistry)
        styles = registry.forInterface(IPortletStyles)
        self.failUnless('portlet_styles' in IPortletStyles)
        self.assertEquals(
            styles.portlet_styles,
            ['noheader|No header', 'nofooter|No footer', 'noheader nofooter|No header and no footer']
        )


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
