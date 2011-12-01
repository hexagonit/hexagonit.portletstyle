# -*- coding: utf-8 -*-
"""Module where test layers and test cases live."""

from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.testing import z2

import unittest2 as unittest


class PortletStyleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import hexagonit.portletstyle
        self.loadZCML(package=hexagonit.portletstyle)
        z2.installProduct(app, 'hexagonit.portletstyle')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'hexagonit.portletstyle:default')

        # Login as Manager
        setRoles(portal, TEST_USER_ID, ('Manager',))

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'hexagonit.portletstyle')


FIXTURE = PortletStyleLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="PortletStyleLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="PortletStyleLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
