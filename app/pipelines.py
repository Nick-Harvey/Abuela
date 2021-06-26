import os
import logging
import python_pachyderm

# Connects to a pachyderm cluster on localhost:30650.
# For other options, see the API docs.
client = python_pachyderm.Client()

class Jaruco():

	def general_restore(uploaded_file):
		"""Do a general restore on a photo that doesn't have cracks"""
		
		with client.commit("general_restore_input", "master") as commit:
		    client.put_file_from_fileobj(commit, "/", uploaded_file)
		pass


	def general_restore_wcracks(uploaded_file):
		"""Do a general restore on a photo that does have cracks"""
		
		with client.commit("general_restore_w_cracks_input", "master") as commit:
		    client.put_file_from_fileobj(commit, "/", uploaded_file)
		pass
