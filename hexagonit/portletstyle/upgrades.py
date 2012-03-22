from Products.CMFCore.utils import getToolByName

import logging

PROFILE_ID = 'profile-hexagonit.portletstyle:default'


def upgrade_0100_to_0101(context, logger=None):
    """Installs qi.portlet.TagClouds"""
    if logger is None:
        # Called as upgrade step: define our own logger.
        logger = logging.getLogger(__name__)

    setup = getToolByName(context, 'portal_setup')
    setup.runAllImportStepsFromProfile('profile-hexagonit.portletstyle:default', purge_old=False)
    logger.info('Installed hexagonit.portletstyle')
