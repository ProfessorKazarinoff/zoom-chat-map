import json
from zoomus import ZoomClient

with open(".zoom_credentials.json","r") as f:
    json_secrets = json.load(f)
    API_KEY = json_secrets['CLIENT_KEY']
    API_SECRET = json_secrets['CLIENT_SECRET']

client = ZoomClient(API_KEY, API_SECRET)

user_list_response = client.user.list()
user_list = json.loads(user_list_response.content)

print(user_list)
