import json
from datetime import datetime

import requests


class ISSAPI:
    """This class will access the ISS API @returns the next date/time
    the station will pass over the lat/long argumaent."""

    def __init__(self, lat_long: tuple[float, float]):

        self.lat = lat_long[0]
        self.long = lat_long[1]

    def get_API(self) -> requests.Response:
        """collects the json file for self.lat long as a parameter."""
        place = {"lat": self.lat, "lon": self.long}
        response = requests.get(
            "http://api.open-notify.org/iss-pass.json", params=place
        )
        return response

    def jprint(self) -> str:
        """@returns the ISS json file in a readable format."""
        # create a formatted string of the Python JSON object
        text = json.dumps(self.get_API(), sort_keys=True, indent=2)
        return text

    def get_date_time(self) -> datetime:
        """@returns the first date time from the json file."""
        response = self.get_API()
        timestamps = response.json()["response"]
        time = datetime.fromtimestamp(timestamps[0].get("risetime"))
        return time
