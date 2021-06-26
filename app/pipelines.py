import os
import logging
import python_pachyderm
from python_pachyderm.service import pps_proto
from python_pachyderm import ModifyFileClient

# Connects to a pachyderm cluster on localhost:30650.
# For other options, see the API docs.
client = python_pachyderm.Client()

class Jaruco():

	def general_restore(uploaded_file):
		"""Do a general restore on a photo that doesn't have cracks"""
		filename = '/{}'.format(uploaded_file.name)
		#img_bytes = uploaded_file.getvalue()
		with client.commit("general_restore_input", "master") as commit:
		    ModifyFileClient.put_file_from_fileobj(commit, filename, uploaded_file)
		pass


	def general_restore_wcracks(uploaded_file):
		"""Do a general restore on a photo that does have cracks"""
		filename = '/{}'.format(uploaded_file.name)
		#img_bytes = uploaded_file.getvalue()
		with client.commit("general_restore_w_cracks_input", "master") as commit:
		    ModifyFileClient.put_file_from_fileobj(commit, filename, uploaded_file)
		pass


	def get_restored_img():
		# # Wait for the commit (and its downstream commits) to finish
		# for _ in client.wait_commit(commit.id):
		#     pass

		# # Get the montage
		# source_file = client.get_file(("montage", "master"), "/montage.png")
		# with tempfile.NamedTemporaryFile(suffix="montage.png", delete=False) as dest_file:
		#     shutil.copyfileobj(source_file, dest_file)
		#     print("montage written to {}".format(dest_file.name))
		pass
