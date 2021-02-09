#!/usr/bin/env python3

import requests, os

#Declare variables to be used
url = "http://localhost/upload/"
user = os.getenv('USER')
image_directory = '/home/{}/supplier-data/images/'.format(user)
files = os.listdir(image_directory)

# Parsing through all the images
for image_name in files:
    # Accepting files that has jpeg extension and ignoring hidden files
    if not image_name.startswith('.') and 'jpeg' in image_name:
        # creating absolute path for each image
        image_path = image_directory + image_name
        # uploading jpeg files
        with open(image_path, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
