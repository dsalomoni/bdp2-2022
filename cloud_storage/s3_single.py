import requests

url = 'CHANGE_ME' # this is the URL of your S3 file (it must be public)
r = requests.get(url)
open('CHANGE_ME', 'wb').write(r.content) # put a name for the output file here