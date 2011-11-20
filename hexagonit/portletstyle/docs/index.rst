.. include:: README.rst

Styling third-party portlets
============================

Follow the steps below to convince your third-party portlets to support
selecting a style for them.

Portlet Assignment
------------------

You portlet's ``Assignment`` class must have an ``__init__()`` and inside this method
it must call base assignment's ``__init__()``. To put it in other words,
``plone.app.portlets.portlets.base.Assignment`` (from which you portlet's
``Assignment`` is likely inheriting from) has an ``__init__()`` method that sets
the ``self.portlet_style`` value. You need to call this ``__init__()`` from your
portlet's assignment's ``__init__()``.

An example of how this can be achieved:

::

    from plone.app.portlets.portlets import base
    class Assignment(base.Assignment):
        implements(IMyCustomPortlet)

        def __init__(self, *args, **kwargs):
            base.Assignment.__init__(self, *args, **kwargs)
            self.foo = kwargs.get('foo', 5)
            self.bar = kwargs.get('bar', "bar")

Portlet AddForm
---------------

Each portlet also has an ``AddForm`` class with a ``create`` method. This method
must also pass the portlet style as a parameter. To make things simpler, just
pass in the entire ``data``.

::

    class AddForm(base.AddForm):
        form_fields = form.Fields(IMyCustomPortlet)

        def create(self, data):
            return Assignment(**data)

Template
--------

Use the style in the template to assign an additional CSS class to your portlet:

::

    <dl class="portlet portletMyCustom"
        tal:attributes="class string:portlet portletMyCustom ${view/portlet_style}"
        i18n:domain="plone">


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

