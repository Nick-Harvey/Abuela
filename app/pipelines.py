import os
import logging
import python_pachyderm

# Connects to a pachyderm cluster on localhost:30650.
# For other options, see the API docs.
client = python_pachyderm.Client()

class Jaruco():

	def general_restore(image):
		"""Do a general restore on a photo that doesn't have cracks"""
		bytes_data = image.getvalue()
		with client.commit("general_restore_input", "master") as commit:
		    client.put_file_bytes(commit, "/", b"bytes_data")
		pass


	def general_restore_wcracks(image):
		"""Do a general restore on a photo that does have cracks"""
		bytes_data = image.getvalue()
		with client.commit("general_restore_w_cracks_input", "master") as commit:
		    client.put_file_bytes(commit, "/", b"bytes_data")
		pass
