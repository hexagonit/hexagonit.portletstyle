from hexagonit.portletclass import HexagonitPortletclassMessageFactory as _
from hexagonit.portletclass.interfaces import IPortletClassSettings
from plone.app.registry.browser import controlpanel


class PortletClassSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IPortletClassSettings
    label = _(u"Portlet Class settings")
    description = _(u"""TODO""")

    def updateFields(self):
        super(PortletClassSettingsEditForm, self).updateFields()

    def updateWidgets(self):
        super(PortletClassSettingsEditForm, self).updateWidgets()


class PortletClassSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = PortletClassSettingsEditForm
