# -*- coding: utf-8 -*-
"""Tests that all of often used portlets are patched."""

from Products.CMFCore.utils import getToolByName
from hexagonit.portletstyle.tests.base import IntegrationTestCase
from plone.app.portlets import portlets
from plone.portlet.collection import collection
from plone.portlet.static import static
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility
from zope.component import queryMultiAdapter
from zope.interface import alsoProvides

import mock
import unittest2 as unittest


class TestPorltets(IntegrationTestCase):
    """Tests patching of often used portlets."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        # apply IPortletStyleLayer browser layer so that z3c.jbot overrides take
        # effect
        from hexagonit.portletstyle.interfaces import IPortletStyleLayer
        alsoProvides(self.layer['app'].REQUEST, IPortletStyleLayer)

        # shortcuts
        self.portal = self.layer['portal']
        self.request = self.portal.REQUEST
        self.view = self.portal.restrictedTraverse('@@plone')
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
        self.manager = getUtility(IPortletManager, name='plone.leftcolumn', context=self.portal)

    def tearDown(self):
        """Cleanup after running tests."""
        # remove all portlets assigned to left column
        for m in self.mapping.keys():
            del self.mapping[m]

    def _add_portlet(self, name=None, assignment_class=None, data=None):
        """A helper method for quickly adding a portlet."""
        portlet = getUtility(IPortletType, name=name)

        data = data or {'portlet_style': 'noheader'}

        addview = self.mapping.restrictedTraverse('+/' + portlet.addview)
        addview.createAndAdd(data=data)

        # is portlet really there?
        assignment = self.mapping.values()[-1]  # portlet is the last in mapping
        self.assertEquals(len(self.mapping), 1)
        self.assertIsInstance(assignment, assignment_class)
        return assignment

    def test_portlet_events(self):
        """Test that events portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='portlets.Events',
            assignment_class=portlets.events.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletEvents noheader">', renderer.render())

    def test_portlet_navigation(self):
        """Test that navigation portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='portlets.Navigation',
            assignment_class=portlets.navigation.Assignment,
            data={
                'portlet_style': 'noheader',
                'topLevel': 0,  # so the portlet is displayed on root
            }
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletNavigationTree noheader">', renderer.render())

    def test_portlet_news(self):
        """Test that news portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='portlets.News',
            assignment_class=portlets.news.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletNews noheader">', renderer.render())

    def test_portlet_recent(self):
        """Test that recent portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='portlets.Recent',
            assignment_class=portlets.recent.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletRecent noheader">', renderer.render())

    @mock.patch('plone.app.portlets.portlets.rss.Renderer.initializing', new=False)
    @mock.patch('plone.app.portlets.portlets.rss.Renderer.enabled', new=True)
    def test_portlet_rss(self):
        """Test that rss portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='portlets.rss',
            assignment_class=portlets.rss.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletRss noheader">', renderer.render())

    def test_portlet_search(self):
        """Test that Search portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='portlets.Search',
            assignment_class=portlets.search.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletSearch noheader">', renderer.render())

    def test_portlet_static(self):
        """Test that static-text portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='plone.portlet.static.Static',
            assignment_class=static.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletStaticText noheader portlet-static-">', renderer.render())

    def test_portlet_collection(self):
        """Test that collection portlet is patched."""
        # add portlet
        portlet = self._add_portlet(
            name='plone.portlet.collection.Collection',
            assignment_class=collection.Assignment
        )

        # what does Renderer.portlet_style give us?
        renderer = queryMultiAdapter((self.portal, self.request, self.view, self.manager, portlet), IPortletRenderer)
        self.assertEquals(renderer.portlet_style(), 'noheader')

        # test HTML
        renderer.update()
        self.assertIn('<dl class="portlet portletCollection noheader portlet-collection-">', renderer.render())


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
