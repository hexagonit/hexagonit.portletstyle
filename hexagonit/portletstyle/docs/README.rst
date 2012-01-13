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

* ``No header``
* ``No footer``
* ``No header and no footer``


Managing available portlet styles
=================================

You can add, edit and remove available portlet styles by going to the `Plone
Control Panel` and clicking on the ``Portlet Styles`` configlet. Pointing your
browser directly to ``http://<zope_ip>:<zope_port>/<plone_id>/@@portletstyles``
also does the trick.

Here, you can enter your styles, one by line, with a pipe (``|``) character
delimiting CSS class and style title. For example, a line ``dummy|Dummy style``
would produce a ``Dummy style`` drop-down menu item that would give the portlet
an additional CSS class of ``foo``.

Lines are checked for formatting and validity of CSS classes. One style can have
multiple CSS classes, for example, the following is valid:
``one two|Double class style``.


Supported portlets
==================

As of this moment, the following portlets are supported (as in, you can select
a style when editing them):

* `Collection portlet`
* `Events portlet`
* `Navigation portlet`
* `News portlet`
* `Recently changed items portlet`
* `RSS portlet`
* `Search portlet`
* `Static text portlet`

The rest of out-of-the-box Plone portlets are non-editable ones as you normally
need only one instance per site. For these (and other) reasons the following
portlets *do not support* choosing a style for them:

* `Calendar portlet`
* `Classic portlet`
* `Language portlet`
* `Login portlet`
* `Review portlet`

