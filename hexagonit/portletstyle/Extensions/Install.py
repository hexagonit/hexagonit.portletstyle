from StringIO import StringIO
from Products.CMFCore.utils import getToolByName


def uninstall(self):
    out = StringIO()
    print >> out, "Removing hexagonit.portletstyle"
    portal_setup = getToolByName(self, 'portal_setup')
    portal_setup.runAllImportStepsFromProfile(
        'profile-hexagonit.portletstyle:uninstall',
        purge_old=False)
