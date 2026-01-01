import json
from google.oauth2 import service_account
from dotenv import load_dotenv
import os

load_dotenv()

def authenticate():
  KEY_PATH = os.getenv("KEY_PATH") # your sample key path

  credentials = service_account.Credentials.from_service_account_file(
      KEY_PATH,
      scopes=["https://www.googleapis.com/auth/cloud-platform"]
  )

  # Extract project ID from the key file
  with open(KEY_PATH) as f:
      key_data = json.load(f)
  PROJECT_ID = key_data["project_id"]

  # CHANGE THIS to your own GCS bucket (must exist and be in europe-west4 for RLHF pipeline)
  STAGING_BUCKET = "gs://rlhf_buck"  # e.g., gs://rlhf-wide-memento-2026

  print(f"Authenticated with service account: {key_data['client_email']}")
  print(f"Project ID: {PROJECT_ID}")
  print(f"Staging bucket: {STAGING_BUCKET}")

  return credentials, PROJECT_ID, STAGING_BUCKET