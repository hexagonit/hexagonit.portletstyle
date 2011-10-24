# -*- coding: utf-8 -*-
"""Tests for portlet style selection on a portlet."""

from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.tests.base import IntegrationTestCase
from plone.app.portlets.portlets import recent
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides

import unittest2 as unittest


class TestSelectStyle(IntegrationTestCase):
    """Tests for portlet style selection on a portlet."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        # apply IPortletStyleLayer browser layer so that z3c.jbot overrides take
        # effect
        from hexagonit.portletstyle.interfaces import IPortletStyleLayer
        alsoProvides(self.layer['app'].REQUEST, IPortletStyleLayer)
        # self.layer['app'].REQUEST['ACTUAL_URL'] = self.layer['app'].REQUEST['URL']

        # shortcuts
        self.request = self.layer['app'].REQUEST
        self.portal = self.layer['portal']
        self.view = self.portal.restrictedTraverse('@@plone')
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
        self.manager = getUtility(IPortletManager, name='plone.leftcolumn')

    def _add_portlet(self, name='portlets.Recent', style=None):
        """A helper method for quickly adding a portlet."""
        style = style or ''
        portlet = getUtility(IPortletType, name=name)
        count = len(self.mapping)

        addview = self.mapping.restrictedTraverse('+/' + portlet.addview)
        addview.createAndAdd(data={'portlet_style': style})

        # is portlet really there?
        assignment = self.mapping.values()[-1]  # portlet is the last in mapping
        self.assertEquals(len(self.mapping), count + 1)
        self.assertIsInstance(assignment, recent.Assignment)
        return assignment

    def test_select_style(self):
        """Test that selected style is present in portlet's HTML."""
        # add portlet
        portlet = self._add_portlet(style='noheader')

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletRecent noheader">', renderer.render())

    def test_no_style_selected(self):
        """Test that nothing breaks if no style was selected."""
        # add portlet
        portlet = self._add_portlet()

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), '')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletRecent ">', renderer.render())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
