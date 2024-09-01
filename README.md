# Short code on how to download a image easily using request module and file handling -> this code involves 
## First install the requests module
```
pip install requests
```
## 1. requesting an image from the website using url -> this process involves use requests module in python to get the response
```
response = requests.get("<website url>")
```
## 2. then writing a file using wb method and saving it in the current dir using file handling
```
with open("<file name>" , "wb" ) as f:
  f.write(response.content)
```
