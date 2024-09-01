import requests

response=requests.get("https://cdn.britannica.com/57/43857-050-9250A718/bar-code.jpg")

with open("img.png","wb") as f:

    f.write(response.content)
