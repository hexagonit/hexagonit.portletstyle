Changelog
---------

1.6 (2012-06-04)
================

- Removed dependency to Products.PloneGazette. [taito]

1.5.1 (2012-05-31)
==================

- Fixed error while adding Subscribe Newsletter Portlet.
  [taito]

1.5 (2012-05-31)
================

- Added portlet form PloneGazette. [taito]
- Removed patching IPortletDataProvider to avoid test failures for portlets.
  [taito]

1.4  (2012-05-24)
===================

- Fixed missing a-tag styling problem [rnd]

1.3.9  (2012-05-21)
===================

- Added conditions for siteurl of rss portlet [rnd]

1.3.8 (2012-03-23)
==================

- Upgrade step for TagClouds [taito]

1.3.7 (2012-03-22)
==================

- Dependency to qi.portlet.TagClouds added to support TagClouds portlet. [taito]

1.3.6 (2012-03-13)
==================

- Customized the collective.quickupload portlet so that the portlet style
  selection gets applied. Previously, the portlet style selection was persisted
  but never used.
  [dokai]

1.3.5 (2012-03-06)
==================

- Dependency to collective.quickupload added. [taito]
- version.txt file removed. [taito]

1.3.4 (2012-02-29)
==================

- Quick Upload patching: made compatible with GS [rnd]

1.3.3 (2012-02-16)
==================

- Quick Upload patching [rnd]
- Added Finnish translations.
  [dokai]

1.3.2 (2012-01-13)
==================

- Patch search portlet.
  [zupo]


1.3.1 (2011-12-02)
==================

- Fixed reStructuredText syntax errors in HISTORY.
  [zupo]


1.3 (2011-12-02)
================

- Don't break portlets if this product is installed in buildout but not
  installed with QuickInstaller.
  [zupo]

- Change default value of portlet_style field to ' ' so it's the same as the
  `Default value` we inject into the drop-down menu.
  [zupo]


1.2 (2011-11-29)
================

- If a portlet has a style assigned that is no longer listed in portlet_styles,
  than it is added to the drop-down menu, so it's still possible to select it.
  [zupo]

- Renamed ``No style`` default style into ``Default style`` and set it as
  default selected value for the Styles drop-down menu.
  [zupo]

- Styles formatting and CSS class validation.
  [zupo]


1.1.1 (2011-11-26)
==================

- Re-releasing because README syntax was broken.
  [zupo]


1.1 (2011-11-26)
================

- Human-readable styles.
  [zupo]

- Improving docs.
  [zupo]


1.0 (2011-11-20)
================

- Slovenian translation.
  [zupo]

- Added translation support for portlet_style field in patched
  IPortletDataProvider.
  [zupo]


1.0a3 (2011-11-07)
==================

- Re-releasing, hoping this fixes problems with jarn.mkrelease.
  [zupo]


1.0a2 (2011-10-27)
==================

- Added whitespace to `.rst` files in docs/ to fix reStucturedText indentation
  errors.
  [zupo]

- Removed ``..code-block::`` elements from README.rst as they are
  Sphinx-specific block elements and are not valid reStucturedText.
  [zupo]


1.0a1 (2011-10-27)
==================

- Initial release.
  [zupo]

