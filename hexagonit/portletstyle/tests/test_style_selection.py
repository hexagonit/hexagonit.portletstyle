# -*- coding: utf-8 -*-
"""Tests for portlet style selection on a portlet."""

from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.tests.base import IntegrationTestCase
from plone.app.portlets.portlets import recent
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility

import unittest2 as unittest


class TestSelectStyle(IntegrationTestCase):
    """Tests for portlet style selection on a portlet."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        # shortcuts
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')

        # remove all portlets already assigned to left column
        for m in self.mapping.keys():
            del self.mapping[m]

    def _add_portlet(self, name='portlets.Recent', style=None):
        style = style or ''
        portlet = getUtility(IPortletType, name=name)

        addview = self.mapping.restrictedTraverse('+/' + portlet.addview)
        addview.createAndAdd(data={'portlet_style': style})

    def test_select_style(self):
        """Test that selected style is present in portlet's HTML."""
        # add portlet
        self._add_portlet(style='noheader')
        self.assertEquals(len(self.mapping), 1)
        self.assertIsInstance(self.mapping.values()[0], recent.Assignment)

        # is portlet really there?
        self.assertEquals(len(self.mapping), 1)
        self.assertIsInstance(self.mapping.values()[0], recent.Assignment)

    def test_no_style_selected(self):
        """Test that nothing breaks if no style was selected."""
        # add portlet
        self._add_portlet(style='noheader')
        self.assertEquals(len(self.mapping), 1)
        self.assertIsInstance(self.mapping.values()[0], recent.Assignment)

        # is portlet really there?
        self.assertEquals(len(self.mapping), 1)
        self.assertIsInstance(self.mapping.values()[0], recent.Assignment)


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
