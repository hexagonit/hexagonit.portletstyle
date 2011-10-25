.. include:: README.rst

Translations
============

Rebuild POT:

.. code-block:: sh

    $ i18ndude rebuild-pot --pot locales/hexagonit.portletstyle.pot --merge locales/manual.pot --create hexagonit.portletstyle .

Sync a translation file with POT:

.. code-block:: sh

    $ find locales -name '*.po' -exec i18ndude sync --pot locales/hexagonit.portletstyle.pot {} \;


.. include:: FUTURE.rst
.. include:: CREDITS.rst
.. include:: HISTORY.rst
.. include:: LICENSE.rst


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

