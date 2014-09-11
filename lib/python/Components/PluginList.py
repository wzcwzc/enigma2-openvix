from MenuList import MenuList

from Tools.Directories import resolveFilename, SCOPE_ACTIVE_SKIN
from Components.MultiContent import MultiContentEntryText, MultiContentEntryPixmapAlphaTest, MultiContentEntryPixmapAlphaBlend

from enigma import eListboxPythonMultiContent, gFont
from Tools.LoadPixmap import LoadPixmap

def PluginEntryComponent(plugin, width=440):
	if plugin.icon is None:
		png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "icons/plugin.png"))
	else:
		png = plugin.icon

	return [
		plugin,
		MultiContentEntryText(pos=(180, 1), size=(width-120, 35), font=0, text=plugin.name),
		MultiContentEntryText(pos=(180, 38), size=(width-120, 25), font=1, text=plugin.description),
		MultiContentEntryPixmapAlphaBlend(pos=(10, 5), size=(150, 60), png = png)
	]

def PluginCategoryComponent(name, png, width=440):
	return [
		name,
		MultiContentEntryText(pos=(110, 15), size=(width-80, 35), font=0, text=name),
		MultiContentEntryPixmapAlphaBlend(pos=(10, 0), size=(90, 75), png = png)
	]

def PluginDownloadComponent(plugin, name, version=None, width=440):
	if plugin.icon is None:
		png = LoadPixmap(resolveFilename(SCOPE_ACTIVE_SKIN, "icons/plugin.png"))
	else:
		png = plugin.icon
	if version:
		if "+git" in version:
			# remove git "hash"
			version = "+".join(version.split("+")[:2])
		elif version.startswith('experimental-'):
			version = version[13:]
		name += "  (" + version + ")"
	return [
		plugin,
		MultiContentEntryText(pos=(110, 1), size=(width-80, 35), font=0, text=name),
		MultiContentEntryText(pos=(110, 38), size=(width-80, 25), font=1, text=plugin.description),
		MultiContentEntryPixmapAlphaBlend(pos=(10, 0), size=(90, 75), png = png)
	]


class PluginList(MenuList):
	def __init__(self, list, enableWrapAround=True):
		MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
		self.l.setFont(0, gFont("Regular", 32))
		self.l.setFont(1, gFont("Regular", 24))
		self.l.setItemHeight(50)
