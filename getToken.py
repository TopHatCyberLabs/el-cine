import requests
import json
import sys

url = 'https://plex.tv/users/sign_in.json'

payload = f'user[login]={sys.argv[1]}&user[password]={sys.argv[2]}'
headers = {
    'X-Plex-Client-Identifier': "1",
    'X-Plex-Product': "Plex Media Server",
    'X-Plex-Version': "1",
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
r = json.loads(response.content)

sys.exit(r['user']['authToken'])
