# main.py

import os
import json
from typing import List

import pandas as pd
from pandas import DataFrame
from requests import Response

from zoom import Zoom

with open(".zoom_credentials.json","r") as f:
    json_secrets = json.load(f)
    ZOOM_API_KEY = json_secrets['API_Key']
    ZOOM_API_SECRET = json_secrets['API_Secret']
    IM_CHAT_HISTORY_TOKEN = json_secrets['IM_Chat_History_Token']
    JWT_TOKEN = json_secrets['JWT_Token']
    ZOOM_MEETING_ID = json_secrets['Meeting_ID']
    ZOOM_MEETING_PASSCODE = json_secrets['Meeting_Passcode']

def main():
    zoom = Zoom(ZOOM_API_KEY, ZOOM_API_SECRET)
    jwt_token: bytes = bytes(JWT_TOKEN,encoding='utf8')
    response: Response = zoom.get_meeting_participants(ZOOM_MEETING_ID, jwt_token)
    print(response)
    list_of_participants: List[dict] = response.json().get("participants")
    while token := response.json().get("next_page_token"):
        response = zoom.get_meeting_participants(ZOOM_MEETING_ID, jwt_token, token)
        list_of_participants += response.json().get("participants")
    df: DataFrame = pd.DataFrame(list_of_participants)

    # output
    print(df.head())


if __name__ == "__main__":
    main()
