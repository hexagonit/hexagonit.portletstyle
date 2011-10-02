from hexagonit.portletstyle import PortletStyleMessageFactory as _
from hexagonit.portletstyle.interfaces import IPortletStyleSettings
from plone.app.registry.browser import controlpanel


class PortletStyleSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPortletStyleSettings
    label = _(u"Portlet Class settings")
    description = _(u"""TODO""")

    def updateFields(self):
        super(PortletStyleSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(PortletStyleSettingsEditForm, self).updateWidgets()


class PortletStyleSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = PortletStyleSettingsEditForm
