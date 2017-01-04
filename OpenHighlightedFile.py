import sublime
import sublime_plugin
import datetime

# Simple plugin that attempts to open the highlighted text as a file in your project directory
class OpenHighlightedFileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Grab all of the highlighted lines
		highlighted_file = ''.join(self.view.substr(l) for l in self.view.sel())

		# Do we have at least one line to work with?
		if len(highlighted_file) > 0:
			# Inform the user what file we are attempting to open
			print("OpenHighlightedFile: Opening {}".format(highlighted_file))
			# Open the file
			self.view.window().open_file(highlighted_file)
		else:
			# Show the console
			self.view.window().run_command("show_panel", { "panel": "console", "toggle": False })
			# Inform the user of the error
			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " | OpenHighlightedFile: Please highlight a file first.")