import os
import sys
import logging

import sublime
import sublime_plugin

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from vendor.djhtml.__main__ import verify_changed
from vendor.djhtml.modes import DjHTML

__version__ = "0.1.0"
__version_info__ = (0, 1, 0)

logger = logging.getLogger("DjHTML")

SUBLIME_SETTINGS = "sublime_djhtml.sublime-settings"


def validate_and_indent(source):
    settings = sublime.load_settings(SUBLIME_SETTINGS)
    tabwidth = settings.get("tabwidth", 4)
    formatted = DjHTML(source).indent(tabwidth)
    if not verify_changed(source, formatted):
        return None

    return formatted


def check_indent_on_save(view):
    settings = sublime.load_settings(SUBLIME_SETTINGS)
    if settings.get("indent_on_save") and view.settings().get("syntax") in settings.get(
        "enabled_syntax", []
    ):
        view.run_command("djhtml_indent")


class DjhtmlIndentCommand(sublime_plugin.TextCommand):
    def run(self, view):
        region = sublime.Region(0, self.view.size())
        source = self.view.substr(region)
        error = None
        try:
            formatted = validate_and_indent(source)
        except Exception:
            error = (
                "DjHTML: An unknown error occured, the template could not be processed."
            )
            logger.exception(error)

        if error:
            sublime.error_message(error)
        elif not formatted:
            sublime.status_message(
                "No indentation required, template file is unchanged."
            )
        else:
            sublime.status_message("Template has been reindented.")
            self.view.replace(view, region, formatted)


class DjhtmlIndentOnSaveListener(sublime_plugin.EventListener):
    def on_pre_save(self, view):
        check_indent_on_save(view)
