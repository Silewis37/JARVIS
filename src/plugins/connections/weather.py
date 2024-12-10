# File Name: weather.py
# Author: Samuel Lewis

#$ TO-DO List $#
#[] TO-DO List Item
#[*] Completed TO-DO List Item

#* Libraries *#

import sys
import os
import requests
from dotenv import load_dotenv

#* Custom Libraries *#

sys.path.append(os.path.abspath("../../"))

#~ import custom made libraries here

#^ Variables ^#

load_dotenv()

ipInfoKey = os.getenv('IPINFO_TOKEN')
OpenWeatherKey = os.getenv('OPEN_WEATHER_TOKEN')

#& Functions &#

def pull_LatLongIP():
  ipinfo_url = f"https://ipinfo.io"
  ipinfo_params = {
    "token": ipInfoKey
  }
  ipinfo_response = requests.get(ipinfo_url, params=ipinfo_params)
  ipinfo_data = ipinfo_response.json()
  coordinates = ipinfo_data['loc'].split(",")
  return coordinates

def get_tomorrow_weather(lat, lon):
    """
    Fetches high and low temperatures for tomorrow using the OpenWeatherMap API.

    Parameters:
        lat(str): the latitude of the location
        lon(str): the longitude of the location

    Returns:
        dict: A dictionary containing tomorrow's weather information or an error message.
    """

    try:
        # Get latitude and longitude
        # Fetch tomorrow's weather
        one_call_url = "https://api.openweathermap.org/data/3.0/onecall"
        one_call_params = {
            "lat": lat,
            "lon": lon,
            "units": "imperial",
            "exclude": "current,minutely,hourly,alerts",
            "appid": OpenWeatherKey
        }
        response = requests.get(one_call_url, params=one_call_params)
        response.raise_for_status()
        data = response.json()

        # Extract tomorrow's weather (index 1 in the daily array)
        tomorrow_weather = data["daily"][1]
        return {
            "High Temp": tomorrow_weather["temp"]["max"],
            "Low Temp": tomorrow_weather["temp"]["min"],
            "Condition": tomorrow_weather["weather"][0]["description"]
        }
    except requests.exceptions.HTTPError as http_err:
        return {"Error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"Error": f"Request error occurred: {req_err}"}


#= Classes =#

#~ define and build classes here

#! Main Program !#

#~ the main program goes here



#- UNASSIGNED COLOR -#
#| UNASSIGNED COLOR |#
#? UNASSIGNED COLOR ?#
#+ UNASSIGNED COLOR +#
#: UNASSIGNED COLOR :#
#; UNASSIGNED COLOR ;#
#% UNASSIGNED COLOR %#
#@ UNASSIGNED COLOR @#