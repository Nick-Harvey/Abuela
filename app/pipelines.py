import os
import logging
import python_pachyderm

# Connects to a pachyderm cluster on localhost:30650.
# For other options, see the API docs.



class Jaruco():

	client = python_pachyderm.Client()
	def general_restore(uploaded_file):
		"""Do a general restore on a photo that doesn't have cracks"""
		filename = '/{}'.format(uploaded_file.name)
		img_bytes = uploaded_file.getvalue()
		with client.commit("general_restore_input", "master") as commit:
		    client.put_files(uploaded_file, commit, filename)
		pass


	def general_restore_wcracks(uploaded_file):
		"""Do a general restore on a photo that does have cracks"""
		filename = '/{}'.format(uploaded_file.name)
		img_bytes = uploaded_file.getvalue()
		with client.commit("general_restore_w_cracks_input", "master") as commit:
		    client.put_files(uploaded_file, commit, filename)
		pass
