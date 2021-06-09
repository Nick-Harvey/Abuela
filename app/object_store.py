import os
import logging
from google.cloud import storage

client = storage.Client

class objectStore():

	def upload_blob(bucket_name, uploaded_file, destination_blob_name):
		"""Uploads a file to the GCS bucket."""

		client = storage.Client()
		bucket = client.get_bucket('dev-abuela-input-images')
		blob = bucket.blob(destination_blob_name)

		blob.upload_from_file(uploaded_file, rewind=True)
		logging.info(
			"File {} uploaded to {}.".format(
				uploaded_file.name, destination_blob_name
				)
			)

