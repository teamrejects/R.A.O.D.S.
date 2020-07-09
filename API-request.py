import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from os.path import abspath
import pprint
import cv2

#_ Data needed__________________________________________________________________________________________________________________________________________________________________________#

path = "/home/ratch8/Documents/ImgClass/Dataset/Test/d.png" # path of image
authenticator = IAMAuthenticator('xxxxxxxxxxxxxxxxxxxxxxxxxxxx') # API key
classifier_ids = ["DefaultCustomModel_xxxxxxxxxxx"] # classifier ID
url = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com/instances/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx' # URl of service

#__Classification and Sorting_______________________________________________________________________________________________________________________________________________________________________________#

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)
visual_recognition.set_service_url(url)
test = abspath(path)
with open(test, 'rb') as images_file:
    Class = visual_recognition.classify(
        images_file=images_file,
        
        classifier_ids=classifier_ids).get_result()
class_val = Class['images'][0]['classifiers'][0]['classes'][0]['class']

#__IMG Processing_______________________________________________________________________________________________________________________________________________________________________________#

print(class_val)
img = cv2.imread(path)

font = cv2.FONT_HERSHEY_SIMPLEX 
text = class_val
org = (16, 45)
fontScale = 2
color = (0, 0, 0) 
thickness = 3
img = cv2.putText(img, text, org, font,  
                   fontScale, color, thickness, cv2.LINE_AA) 

cv2.imshow('img',img)
cv2.waitKey()





































































