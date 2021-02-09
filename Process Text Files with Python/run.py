#! /usr/bin/env python3

#import necessary python modules
import os
import requests

#Variable declaration
path = '/data/feedback/'
myLink = 'http://<External-IP-Address>/feedback/'
myFiles = os.listdir(path)

#Enter for-loop to process files
for file in myFiles:
        #Open files and process data within
        myData = open(path + file)
        iData = myData.read().split('\n')

        #Create dictionary of the retreaved data
        myDictionary = {"title":iData[0], "name":iData[1], "date":iData[2], "feedback":iData[3]}

        #Upload the feedback to the website
        response = requests.post(myLink, json=myDictionary)

        #Close the files
        myData.close()

print(response.status_code)
