'''
TODO: 
1. How to get the lines/blocks of text only and not the single words at the end of output file?
2. Figure out how to remove output.seek(0) so that you do it all in one code block or close and reopen file from beginning?
'''

import json
import os
import io
from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account

config_path = os.path.join("..", "config.json")

google_creds_path = os.path.join("c:/", "Users", "mdabler", "OneDrive - Rightpoint", "Desktop", "beer-recommendation-app-3764c8dfdd8e.json")

google_creds = service_account.Credentials.from_service_account_file(google_creds_path)

with open(config_path) as json_data_file:
    config_data = json.load(json_data_file)

''' Set up connection to Google Vision API '''
# Instantiates a client
client = vision.ImageAnnotatorClient(credentials=google_creds)

# The name of the image file to annotate
file_name = os.path.join("..", "Resources", "Images", "beer_menu_1.png")

# def detect_text(path):
#     """Detects text in the file."""
#     from google.cloud import vision
#     client = vision.ImageAnnotatorClient()

#     with io.open(path, 'rb') as image_file:
#         content = image_file.read()

#     image = vision.types.Image(content=content)

#     response = client.text_detection(image=image)
#     texts = response.text_annotations
#     print('Texts:')

#     for text in texts:
#         print('\n"{}"'.format(text.description))

#         vertices = (['({},{})'.format(vertex.x, vertex.y)
#                     for vertex in text.bounding_poly.vertices])

#         print('bounds: {}'.format(','.join(vertices)))

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.text_detection(image=image)
texts = response.text_annotations

output = open("output.txt", "a+")

for text in texts:
    output.write(str('{}'.format(text.description)))

output.seek(0)
lineList = [line.rstrip('\n') for line in output]
print(lineList)

output.close()


# print('Texts:')

# for text in texts:
#     print('\n"{}"'.format(text.description))

#     vertices = (['({},{})'.format(vertex.x, vertex.y)
#                 for vertex in text.bounding_poly.vertices])

#     print('bounds: {}'.format(','.join(vertices)))

# Set up connection to GCP Datastore

# Set up connection to Untappd API

# Send image file to Google Vision API and get response

# Sort response into likely beer names based on comparing names with close matches in GCP beer name datastore

# Use the matched beer names to call the Untappd API

# Print out matches by showing name, rating, and ABV