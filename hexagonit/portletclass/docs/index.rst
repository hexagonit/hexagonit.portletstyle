.. include:: README.rst
.. include:: FUTURE.rst
.. include:: CREDITS.rst
.. include:: HISTORY.rst
.. include:: LICENSE.rst

Translations
============

Rebuild POT:

.. code-block:: sh

    $ i18ndude rebuild-pot --pot locales/hexagonit.portletclass.pot --merge locales/manual.pot --create hexagonit.portletclass .

Sync a translation file with POT:

.. code-block:: sh

    $ find locales -name '*.po' -exec i18ndude sync --pot locales/hexagonit.portletclass.pot {} \;

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

