import sublime
import sublime_plugin
from sublime import load_settings

from .vendor.djhtml.modes import DjHTML

SETTINGS = load_settings("sublime_djhtml.sublime-settings")


class DjhtmlIndentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        tabwidth = SETTINGS.get("tabwidth", 4)
        region = sublime.Region(0, self.view.size())
        file_data = self.view.substr(region)
        self.view.replace(edit, region, DjHTML(file_data).indent(tabwidth))


class DjhtmlIndentOnSaveListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        if SETTINGS.get("indent_on_save") and view.settings().get(
            "syntax"
        ) in SETTINGS.get("enabled_syntax", []):
            view.run_command("djhtml_indent")
