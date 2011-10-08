# -*- coding: utf-8 -*-
"""Tests for portlet style selection on a portlet."""

from hexagonit.portletstyle.tests.base import IntegrationTestCase
from Products.CMFCore.utils import getToolByName
from plone.portlets.interfaces import IPortletType
from zope.component import getUtility
from plone.app.portlets.portlets import recent

import unittest2 as unittest


class TestSelectStyle(IntegrationTestCase):
    """Tests for portlet style selection on a portlet."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        # shortcuts
        self.portal = self.layer['portal']
        self.installer = getToolByName(self.portal, 'portal_quickinstaller')
        
        # remove all portlets already assigned to left column
        mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
        for m in mapping.keys():
            del mapping[m]

        # add recent-items portlet
        portlet = getUtility(IPortletType, name='portlets.Recent')
        addview = mapping.restrictedTraverse('+/' + portlet.addview)
        addview.createAndAdd(data={})
        self.assertEquals(len(mapping), 1)
        self.assertTrue(isinstance(mapping.values()[0], recent.Assignment))


    def test_foo(self):
        print 'a'


def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above."""
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
