import base64
import json
import os

from google.cloud import storage
from google.cloud import vision
# from google.oauth2 import service_account

vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()

with open("config.json") as f:
    data = f.read()
config = json.loads(data)

# google_creds_path = os.path.join("c:/", "Users", "mdabler", "OneDrive - Rightpoint", "Desktop", "beer-recommendation-app-3764c8dfdd8e.json")
# google_creds = service_account.Credentials.from_service_account_file(google_creds_path)

def process_image(file, context):
    """Cloud Function triggered by Cloud Storage when a file is changed.
    Args:
        file (dict): Metadata of the changed file, provided by the triggering
                                 Cloud Storage event.
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to stdout and Stackdriver Logging
    """
    bucket = validate_message(file, 'bucket')
    name = validate_message(file, 'name')

    detect_text(bucket, name)

    print('File {} processed.'.format(file['name']))

def detect_text(bucket, filename):
    print('Looking for text in image {}'.format(filename))

    text_detection_response = vision_client.text_detection({
        'source': {'image_uri': 'gs://{}/{}'.format(bucket, filename)}
    })
    annotations = text_detection_response.text_annotations
    if len(annotations) > 0:
        text = annotations[0].description
    else:
        text = ''
    print('Extracted text {} from image ({} chars).'.format(text, len(text)))

def save_result(event, context):
    if event.get('data'):
        message_data = base64.b64decode(event['data']).decode('utf-8')
        message = json.loads(message_data)
    else:
        raise ValueError('Data sector is missing in the Pub/Sub message.')

    text = validate_message(message, 'text')
    filename = validate_message(message, 'filename')

    print('Received request to save file {}.'.format(filename))

    bucket_name = config['RESULT_BUCKET']
    result_filename = '{}.txt'.format(filename)
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(result_filename)

    print('Saving result to {} in bucket {}.'.format(result_filename,
                                                     bucket_name))

    blob.upload_from_string(text)

    print('File saved.')

def validate_message(message, param):
    var = message.get(param)
    if not var:
        raise ValueError('{} is not provided. Make sure you have \
                          property {} in the request'.format(param, param))
    return var