import requests,json

url = 'http://127.0.0.1:5000/fury'



x = requests.post(url, files={"file":open("tt.wav","rb") })

print(x.text)

