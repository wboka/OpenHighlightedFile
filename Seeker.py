import sublime
import sublime_plugin
import datetime
import re
import webbrowser

# Seeker: Sublime Text plugin that finds any links in the current file. Limited to the following attributes: href, src, and template

class SeekerLinksCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Placeholder for any links
		self.links = []
		# Find all links to other pages/websites.
		self.view.find_all("((?:src|href|template)=\".*\")", 0, "$1", self.links)

		# Placeholder for cleaned up links
		stripped_lines = []

		for l in self.links:
			# Split links on '" '
			new_line = l.split("\" ")[0]
			# Remove any unnecessary fluff
			new_line = re.sub("\"|^src=|^href=|^template=", "", new_line)
			# Add to stripped_lines
			stripped_lines.append(new_line)

		# Update self.links
		self.links = stripped_lines

		# Do we have more than 1 link?
		if len(self.links) > 0:
			# Display links in a quick panel
			self.view.window().show_quick_panel(self.links, self.insert_link)
		else:
			# No links. Alert the user
			self.view.window().run_command("show_panel", { "panel": "console", "toggle": False })

			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " | Seeker: No links found.")

	def insert_link(self, choice):
		if choice == -1:
			# Log the lack of selected link
			# self.view.window().run_command("show_panel", { "panel": "console", "toggle": False })
			print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " | Seeker: No link selected.")

			return

		# Is the link to an external website?
		if re.search("http|git", self.links[choice]):
			# Open it in the user's default browser
			print("Opening {} in your default web browser".format(self.links[choice]))

			webbrowser.open(self.links[choice])
		else:
			# Open the file in the editor or create a new tab for it
			print("Opening {}".format(self.links[choice]))

			self.view.window().open_file(self.links[choice])
