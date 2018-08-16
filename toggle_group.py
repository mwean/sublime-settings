import sublime, sublime_plugin


class ToggleGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        new_group = 0 if sublime.Window.active_group(sublime.active_window()) == 1 else 1
        sublime.active_window().focus_group(new_group)
