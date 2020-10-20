# google_maps_api.py
"""
A Python module that holds functions to create API calls to the Google maps API
"""

import json

with open(".google_credentials.json","r") as f:
    json_secrets = json.load(f)
    MAPS_API_KEY = json_secrets['MAPS_API_KEY']
"""
https://maps.googleapis.com/maps/api/staticmap?center=Lebanon+Kansas&zoom=3&size=400x290&maptype=roadmap&markers=color:blue|label:R|40.702147,-74.015794&markers=color:green|label:G|40.711614,-74.012318&markers=color:red|label:C|40.718217,-73.998284&key=AIzaSyC9t4l2qY7byspD1d8_Hws0B5pSgw4oeWE
"""

class GoogleMapsStaticURL():

    def __init__(self):
        BASE_URL = "https://maps.googleapis.com/maps/api/staticmap"
        self.base_url = BASE_URL

    def add_center(self, location:str, city:str, state:str):
        self.center = f"?center={location},{city},{state}"

    def add_zoom(self, zoom:int):
        self.zoom = f"&zoom={zoom}"

    def add_size(self, width:int, height:int):
        self.size = f"&size={width}x{height}"

    def add_maptype(self, maptype:str):
        self.maptype = f"&maptype={maptype}"

    def add_marker(self, marker_color:str, marker_label:str, marker_lat:str, marker_lon:str):
        self.marker = f"&markers=color:{marker_color}label:{marker_label}{marker_lat}{marker_lon}"

    def add_api_key(self, api_key:str):
        self.api_key = f"&key={api_key}"

    def get_url(self):
        return f"{self.base_url}{self.center}{self.zoom}{self.size}{self.maptype}{self.marker}{self.api_key}"

    def __str__(self):
        return self.get_url()

    def __repr__(self):
        return self.get_url()
