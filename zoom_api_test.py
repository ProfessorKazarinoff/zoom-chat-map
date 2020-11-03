import http.client
import json
import requests

with open(".zoom_credentials.json","r") as f:
    json_secrets = json.load(f)
    ZOOM_API_KEY = json_secrets['API_Key']
    ZOOM_API_SECRET = json_secrets['API_Secret']
    IM_CHAT_HISTORY_TOKEN = json_secrets['IM_Chat_History_Token']
    JWT_TOKEN = json_secrets['JWT_Token']
    ZOOM_MEETING_ID = json_secrets['Meeting_ID']
    ZOOM_MEETING_PASSCODE = json_secrets['Meeting_Passcode']
    ZOOM_USER_ID = json_secrets['User_ID']

authorization_string = f'Bearer {JWT_TOKEN}'

headers = {
    'authorization': authorization_string,
    'content-type': "application/json"
    }


url = "https://api.zoom.us/v2/users?status=active&page_size=30&page_number=1"

r = requests.get(url,headers=headers)
print(r.text)
print(r.json())
print(type(r.json()))

url2 = f'https://api.zoom.us/v2/chat/users/{ZOOM_USER_ID}/messages'
headers2 = {
    'content-type': "application/json",
    'authorization': authorization_string
    }

r2 = requests.post(url=url2,json={"message": "It's a beautiful day."},headers=headers2)
print(r2.text)
