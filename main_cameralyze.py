import base64 
import requests 

with open("test_1.jpg", "rb") as image_file: 
  encoded_string = base64.b64encode(image_file.read()).decode("utf8")

api_call = requests.post("https://api.server.cameralyze.co/836586f0-b309-4995-af2f-ac43d78273fa", json={"apiKey": "01uqJH02713ZKYYB", "image": encoded_string})

if api_call.status_code == 200:
    print(api_call.json()) 
else:
    print(api_call.status_code)
    print(api_call.text)