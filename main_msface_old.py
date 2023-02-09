import asyncio
import io
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, QualityForRecognition


# This key will serve all examples in this document.
KEY = "17a23b938c7b4ff5b3f5636043495412"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://crowdmanagement-face.cognitiveservices.azure.com/"

# Base url for the Verify and Facelist/Large Facelist operations
#IMAGE_BASE_URL = 'https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/Face/images/'

test_image = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/Face/images/identification1.jpg"


face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

faces = face_client.face.detect_with_url(test_image,
                                         detection_model='detection_03',
                                         recognition_model='recognition_04',
                                         return_face_attributes=['qualityForRecognition']
                                        )

print(faces)
"[?returnFaceId][&returnFaceLandmarks][&returnFaceAttributes][&recognitionModel][&returnRecognitionModel][&detectionModel][&faceIdTimeToLive]"