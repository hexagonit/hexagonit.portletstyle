===============================
Assign a CSS style to a portlet
===============================

`hexagonit.portletstyle` is a Plone 4.x add-on that allows you to assign a CSS
style to a portlet. You can chose from a list of pre-defined (configurable
through Plone Control Panel) classes.

* `Source code @ GitHub <http://github.com/hexagonit/hexagonit.portletstyle>`_
* `Releases @ PyPI <http://pypi.python.org/pypi/hexagonit.portletstyle>`_
* `Sphinx docs @ ReadTheDocs <http://readthedocs.org/docs/hexagonitportletstyle>`_


Installation
============

To install ``hexagonit.portletstyle`` you simply add
``hexagonit.portletstyle`` to the list of eggs in your buildout, run
buildout and restart Plone. Then, install `hexagonit.portletstyle` using the
Add-ons control panel.


Usage
=====

Click on ``Manage portlets`` and add or edit a portlet. Select your desired
portlet style from the `Portlet Style` drop-down menu and save. That's it.


Default portlet styles
======================

By default, this package gives you three default portlet styles:

* ``noheader``
* ``nofooter``
* ``noheader nofooter``


Managing available portlet styles
=================================

You can add, edit and remove available portlet styles by going to the `Plone
Control Panel` and clicking on the ``Portlet Styles`` configlet. Pointing your
browser directly to ``http://<zope_ip>:<zope_port>/<plone_id>/@@portletstyles``
also does the trick.


Supported portlets
==================

As of this moment, the following portlets are supported (as in, you can select
a style when editing them):

* `Events portlet`
* `Navigation portlet`
* `News portlet`
* `Recently changed items portlet`
* `RSS portlet`
* `Collection portlet`
* `Static text portlet`

The rest of out-of-the-box Plone portlets are non-editable ones as you normally
need only one instance per site. For these (and other) reasons the following
portlets *do not support* choosing a style for them:

* `Calendar portlet`
* `Classic portlet`
* `Language portlet`
* `Login portlet`
* `Review portlet`
* `Search portlet`


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

