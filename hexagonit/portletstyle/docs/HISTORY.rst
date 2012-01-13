Changelog
=========

1.3.2 (2012-01-13)
------------------

- Patch search portlet.
  [zupo]


1.3.1 (2011-12-02)
------------------

- Fixed reStructuredText syntax errors in HISTORY.
  [zupo]


1.3 (2011-12-02)
----------------

- Don't break portlets if this product is installed in buildout but not
  installed with QuickInstaller.
  [zupo]

- Change default value of portlet_style field to ' ' so it's the same as the
  `Default value` we inject into the drop-down menu.
  [zupo]


1.2 (2011-11-29)
----------------

- If a portlet has a style assigned that is no longer listed in portlet_styles,
  than it is added to the drop-down menu, so it's still possible to select it.
  [zupo]

- Renamed ``No style`` default style into ``Default style`` and set it as
  default selected value for the Styles drop-down menu.
  [zupo]

- Styles formatting and CSS class validation.
  [zupo]


1.1.1 (2011-11-26)
------------------

- Re-releasing because README syntax was broken.
  [zupo]


1.1 (2011-11-26)
----------------

- Human-readable styles.
  [zupo]

- Improving docs.
  [zupo]


1.0 (2011-11-20)
----------------

- Slovenian translation.
  [zupo]

- Added translation support for portlet_style field in patched
  IPortletDataProvider.
  [zupo]


1.0a3 (2011-11-07)
------------------

- Re-releasing, hoping this fixes problems with jarn.mkrelease.
  [zupo]


1.0a2 (2011-10-27)
------------------

- Added whitespace to `.rst` files in docs/ to fix reStucturedText indentation
  errors.
  [zupo]

- Removed ``..code-block::`` elements from README.rst as they are
  Sphinx-specific block elements and are not valid reStucturedText.
  [zupo]


1.0a1 (2011-10-27)
------------------

- Initial release.
  [zupo]

