import os
import logging
from google.cloud import storage

client = storage.Client

class objectStore():

	def upload_blob(bucket_name, uploaded_file, destination_blob_name):
		"""Uploads a file to the GCS bucket."""
		#TODO Add something to check if the file has already be added in the last 60 seconds

		client = storage.Client()
		bucket = client.get_bucket('abuela_input_images_dev')
		blob = bucket.blob(destination_blob_name)

		blob.upload_from_file(uploaded_file, rewind=True)
		logging.info(
			"File {} uploaded to {}.".format(
				uploaded_file.name, destination_blob_name
				)
			)

