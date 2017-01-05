import sublime
import sublime_plugin
import datetime

# Simple plugin that attempts to open the highlighted text as a file in your project directory
class OpenHighlightedFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		lines = []

		for selectedRegion in self.view.sel():
			selectedLines = self.view.lines(selectedRegion)

			for line in selectedLines:
				 lines.append(self.view.substr(line))

		# Do we have at least one line to work with?
		if len(lines) == 1:
			# Only one, open the file or open a new tab to create it
			self.view.window().open_file(lines[0])
		elif len(lines) > 0:
			# Open a quick panel containing the selected file names
			self.view.window().show_quick_panel(lines, lambda i: self.view.window().open_file(lines[i]))
		else:
			# Show the console
			self.view.window().run_command("show_panel", { "panel": "console", "toggle": False })
			# Inform the user of the error
			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " | OpenHighlightedFile: Please highlight a file first.")
