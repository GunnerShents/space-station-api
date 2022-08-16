import json

import requests


class AccessMapBox:
    """AccessMapBox locates and retruns a latitude and longitude rounded when you run the .get_lat_long
    method entering the place you require as an argument."""

    def __init__(self):

        self.place = ""
        self.token = "pk.eyJ1IjoiZ3VubmVyc2hlbnRzIiwiYSI6ImNsNWtzOGxnejBkMGIzY280NjJ4NWpzYW0ifQ.cIj029e2KzRQT67nNo76Rw"
        self.lat_long: tuple[float, float] = ()

    def collect_mapBox_API(self) -> str | int:
        """Collects the API from MapBox using the place and self.token"""
        try:
            self.response = requests.get(
                f"https://api.mapbox.com/geocoding/v5/mapbox.places/{self.place}.json?access_token={self.token}"
            )
            code = self.response.status_code
            return code
        except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
        except requests.exceptions.ConnectionError as errc:
            return "An Error Connecting to the API occurred:" + repr(errc)
        except requests.exceptions.Timeout as errt:
            return "A Timeout Error occurred:" + repr(errt)
        except requests.exceptions.RequestException as err:
            return "An Unknown Error occurred" + repr(err)

    def jprint(self, obj: requests.Response) -> str:
        """@returns a created formatted string of the Python JSON object"""
        text = json.dumps(obj, sort_keys=True, indent=2)
        return text

    def set_lat_long(self) -> None:
        """Locates and sets the lat and long for the stroed Json file.
        rounds the floats and stores them in the class tuple."""
        a = self.response.json()
        round_to = 3
        # locates the coordinates in the json file by slicing through the
        # dictionaries and lists
        x, y = a.get("features")[0].get("geometry").get("coordinates")
        self.lat_long = round(x, round_to), round(y, round_to)

    def get_lat_long(self, place: str) -> tuple[float, float]:
        """This is them main method for the class, this will collect the API from mapbox
        locate the latitude and longitude for the selected place
        @arg is the location name
        @returns the lat long"""
        self.place = place
        self.collect_mapBox_API()
        self.set_lat_long()
        return self.lat_long
