import requests, json, base64

API_KEY = 'your key'
API_SECRET = 'your secret'
image_path = "people.jpg"  # change this to your image's path

host = "https://api-us.idphotoapp.com"
url = host + "/v2/makeIdPhoto"

if __name__ == '__main__':
   with open(image_path, 'rb') as f:
      pic = f.read()

   data = {
      "specCode": "australia-passport",
      "imageBase64": base64.b64encode(pic).decode(),
      "apiKey": API_KEY,
      "apiSecret": API_SECRET
   }
   data_json = json.dumps(data)
   response = requests.post(url, data=data_json)
   print(response.json())
