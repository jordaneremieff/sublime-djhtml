import os
import sys
import sublime
import sublime_plugin


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vendor.djhtml.modes import DjHTML


SUBLIME_SETTINGS = "sublime_djhtml.sublime-settings"


class DjhtmlIndentCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = sublime.load_settings(SUBLIME_SETTINGS)
        tabwidth = settings.get("tabwidth", 4)
        region = sublime.Region(0, self.view.size())
        file_data = self.view.substr(region)
        indented = DjHTML(file_data).indent(tabwidth)
        self.view.replace(edit, region, indented)


class DjhtmlIndentOnSaveListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        settings = sublime.load_settings(SUBLIME_SETTINGS)
        if settings.get("indent_on_save") and view.settings().get(
            "syntax"
        ) in settings.get("enabled_syntax", []):
            view.run_command("djhtml_indent")
