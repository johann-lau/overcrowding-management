import requests

BASE_URL = "https://crowdmanagement-face.cognitiveservices.azure.com/face/v1.0/detect"

HEADERS = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': "17a23b938c7b4ff5b3f5636043495412"
}

PARAMS = {
    'returnFaceLandmarks': 'true',
    'returnFaceId': 'true',
    'detectionModel': 'detection_03',
}

url = "https://u.cubeupload.com/Johann/test1.jpg"

data = {'url': url}

r = requests.post(BASE_URL, data=data, headers=HEADERS, params=PARAMS)


print(r.json())
print(r.status_code)