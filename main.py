#googlecloudvisionstuff
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='vision_key.json'
from google.cloud import vision
import re 
import io

vision_client = vision.ImageAnnotatorClient()
image = vision.Image()

image_path = r'C:\Users\johns\Desktop\Root\Projects\Text Extraction using Tesseract\images\B\1.jpg'

with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

image = vision.Image(content=content)

response = vision_client.text_detection(image=image)

text = response.text_annotations[0].description

print(text)