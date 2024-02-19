import json
import requests

url = "https://ocr.asprise.com/api/v1/receipt"

image = "test_files/receipt1.jpg"

res = requests.post(url, data = {
  "api_key": "TEST",
  "recognizer": "auto",
  "ref_no": "ocr_python_123"
}, files = { "file": open(image, "rb")})

with open("test_files/res1.json", "w") as file:
  json.dump(json.loads(res.text), file)
