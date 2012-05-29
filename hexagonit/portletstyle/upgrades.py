from Products.CMFCore.utils import getToolByName

import logging

PROFILE_ID = 'profile-hexagonit.portletstyle:default'


def reimport_package(context, logger=None):
    """Reimport hexagonit.portletstyle."""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-hexagonit.portletstyle:default', purge_old=False)
    logger.info('Installed hexagonit.portletstyle')
