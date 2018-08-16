import sublime
import sublime_plugin
import re

class TogglePrintCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    view = self.view
    index = view.sel()[0].a
    line_region = view.line(index)
    line = view.substr(line_region)

    if re.match(r"^\s*p\s+", line):
      new_line = re.sub(r"(^\s*)p ", "\\1", line)
      index_change = -2
    else:
      new_line = 'p ' + line
      index_change = 2

    new_index = index + index_change

    view.replace(edit, line_region, new_line)
    view.sel().clear()
    view.sel().add(sublime.Region(new_index, new_index))
