# -*- coding: utf-8 -*-
"""Control panel configlet for configuring available portlet styles."""

from hexagonit.portletstyle import PortletStyleMessageFactory as _
from hexagonit.portletstyle.interfaces import IPortletStyles
from plone.app.registry.browser import controlpanel
from plone.z3cform.textlines import TextLinesFieldWidget


class PortletStylesEditForm(controlpanel.RegistryEditForm):

    schema = IPortletStyles
    label = _(u"Portlet Styles")

    def updateFields(self):
        super(PortletStylesEditForm, self).updateFields()

    def updateWidgets(self):
        self.fields["portlet_styles"].widgetFactory = TextLinesFieldWidget
        super(PortletStylesEditForm, self).updateWidgets()


class PortletStylesControlPanel(controlpanel.ControlPanelFormWrapper):
    form = PortletStylesEditForm
