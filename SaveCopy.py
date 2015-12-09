import sublime, sublime_plugin
import os

# Class for the save_copy command
class SaveCopyCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Dateinamen holen und pruefen
		fileName = self.view.file_name()
		if fileName == None:
			sublime.error_message("You have to save the file first!")
			return

		# get content of the file
		allcontent = self.view.substr(sublime.Region(0, self.view.size()))

		# create new file
		newFile = self.view.window().new_file()
		newFile.run_command("write", {"textBuffer" : allcontent})
		newFile.retarget(fileName)

		# save the new file with prompt for file name and path
		newFile.run_command("prompt_save_as")

		# close new file silently
		newFile.set_scratch(True)
		newFile.close()

		# focus the original file
		self.view.window().focus_view(self.view)

# Class for the write command for writing the content in the new file
class WriteCommand(sublime_plugin.TextCommand):
	def run(self, edit, textBuffer):
		self.view.insert(edit, 0, textBuffer)
