# Short code to download a image easily -> this code involves 
# requesting an image from the website using url -> this process involves use requests module in python to get to response
# then writing a file using wb method and saving it in the current dir using file handling


import requests

response=requests.get("https://cdn.britannica.com/57/43857-050-9250A718/bar-code.jpg")
with open("img.png","wb") as f:
    f.write(response.content)