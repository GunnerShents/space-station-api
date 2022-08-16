from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from ISSapp.forms import SelectCityForm
from ISSapp.geo import AccessMapBox
from ISSapp.stationapi import ISSAPI


def index(request: HttpRequest) -> HttpResponse:
    """This view checks the request method and @returns
    a render function back to the same page"""
    if request.method == "POST":
        form = SelectCityForm()
        mapping = AccessMapBox()
        text = request.POST["city"]
        coords = mapping.get_lat_long(text)
        station_api = ISSAPI(coords)
        time = station_api.get_date_time()
        return render(
            request,
            "ISSapp/index.html",
            {"form": form, "text": text, "coords": coords, "time": time},
        )
    else:
        form = SelectCityForm()
        print("page loaded!")
        return render(request, "ISSapp/index.html", {"form": form})
