import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import os
import time
import sys

# List of cities with their coordinates
cities = [
    # EU
    # {"country": "united_kingdom", "city": "london", "latitude": 51.5074, "longitude": -0.1278},
    # {"country": "united_kingdom", "city": "manchester", "latitude": 53.4808, "longitude": -2.2426},
    # {"country": "united_kingdom", "city": "edinburgh", "latitude": 55.9533, "longitude": -3.1883},
    #
    # {"country": "france", "city": "paris", "latitude": 48.8566, "longitude": 2.3522},
    # {"country": "france", "city": "marseille", "latitude": 43.2965, "longitude": 5.3698},
    # {"country": "france", "city": "nice", "latitude": 43.7102, "longitude": 7.2620},
    #
    # {"country": "germany", "city": "berlin", "latitude": 52.5200, "longitude": 13.4050},
    # {"country": "germany", "city": "hamburg", "latitude": 53.5511, "longitude": 9.9937},
    # {"country": "germany", "city": "munich", "latitude": 48.1351, "longitude": 11.5820},
    #
    # {"country": "italy", "city": "rome", "latitude": 41.9028, "longitude": 12.4964},
    # {"country": "italy", "city": "milan", "latitude": 45.4642, "longitude": 9.1900},
    # {"country": "italy", "city": "naples", "latitude": 40.8518, "longitude": 14.2681},
    #
    # {"country": "spain", "city": "madrid", "latitude": 40.4168, "longitude": -3.7038},
    # {"country": "spain", "city": "barcelona", "latitude": 41.3851, "longitude": 2.1734},
    # {"country": "spain", "city": "valencia", "latitude": 39.4699, "longitude": -0.3763},
    #
    # {"country": "netherlands", "city": "amsterdam", "latitude": 52.3676, "longitude": 4.9041},
    # {"country": "netherlands", "city": "rotterdam", "latitude": 51.9225, "longitude": 4.4791},
    #
    # {"country": "switzerland", "city": "zurich", "latitude": 47.3769, "longitude": 8.5417},
    # {"country": "switzerland", "city": "geneva", "latitude": 46.2044, "longitude": 6.1432},
    #
    # {"country": "sweden", "city": "stockholm", "latitude": 59.3293, "longitude": 18.0686},
    # {"country": "sweden", "city": "gothenburg", "latitude": 57.7089, "longitude": 11.9746},
    #
    # {"country": "norway", "city": "oslo", "latitude": 59.9139, "longitude": 10.7522},
    # {"country": "norway", "city": "bergen", "latitude": 60.3913, "longitude": 5.3221},
    #
    # {"country": "denmark", "city": "copenhagen", "latitude": 55.6761, "longitude": 12.5683},
    #
    # {"country": "austria", "city": "vienna", "latitude": 48.2082, "longitude": 16.3738},
    #
    # {"country": "belgium", "city": "brussels", "latitude": 50.8503, "longitude": 4.3517},
    #
    # {"country": "ireland", "city": "dublin", "latitude": 53.3498, "longitude": -6.2603},
    #
    # {"country": "finland", "city": "helsinki", "latitude": 60.1699, "longitude": 24.9384},
    #
    # {"country": "greece", "city": "athens", "latitude": 37.9838, "longitude": 23.7275},
    #
    # {"country": "poland", "city": "warsaw", "latitude": 52.2297, "longitude": 21.0122},
    #
    # {"country": "portugal", "city": "lisbon", "latitude": 38.7169, "longitude": -9.1399},
    #
    # {"country": "czech_republic", "city": "prague", "latitude": 50.0755, "longitude": 14.4378},
    #
    # {"country": "hungary", "city": "budapest", "latitude": 47.4979, "longitude": 19.0402},
    #
    # {"country": "romania", "city": "bucharest", "latitude": 44.4268, "longitude": 26.1025},
    #
    # {"country": "croatia", "city": "zagreb", "latitude": 45.8150, "longitude": 15.9819},
    #
    # {"country": "russia", "city": "moscow", "latitude": 55.7558, "longitude": 37.6173},
    # {"country": "russia", "city": "saint_petersburg", "latitude": 59.9343, "longitude": 30.3351},
    #
    # {"country": "cyprus", "city": "nicosia", "latitude": 35.1856, "longitude": 33.3823},
    #
    # {"country": "iceland", "city": "reykjavik", "latitude": 64.1355, "longitude": -21.8954},
    #
    # {"country": "slovenia", "city": "ljubljana", "latitude": 46.0569, "longitude": 14.5058},
    #
    # {"country": "bulgaria", "city": "sofia", "latitude": 42.6977, "longitude": 23.3219},
    #
    # {"country": "slovakia", "city": "bratislava", "latitude": 48.1486, "longitude": 17.1077},
    #
    # {"country": "ukraine", "city": "kyiv", "latitude": 50.4501, "longitude": 30.5234},
    #
    # {"country": "belarus", "city": "minsk", "latitude": 53.9045, "longitude": 27.5615},

    # Latin America
    # East Asia
    # Oceania Pacific
]

# Set up the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Base directory for storing the data
base_dir = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API'

# Ensure the base directory exists
os.makedirs(base_dir, exist_ok=True)

# Function to fetch and save daily weather data
def fetch_and_save_daily_weather(city_info):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": city_info["latitude"],
        "longitude": city_info["longitude"],
        "start_date": "2014-07-09",
        "end_date": "2024-07-10",
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", "temperature_2m_mean",
                  "apparent_temperature_max", "apparent_temperature_min", "apparent_temperature_mean",
                  "sunrise", "sunset", "daylight_duration", "sunshine_duration", "precipitation_sum",
                  "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max",
                  "wind_gusts_10m_max", "wind_direction_10m_dominant", "et0_fao_evapotranspiration"],
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process response data
    response = responses[0]
    daily = response.Daily()
    date_range = pd.date_range(
        start=pd.to_datetime(daily.Time(), unit="s", utc=True),
        end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=daily.Interval()),
        inclusive="left"
    )
    daily_data = {"date": date_range.strftime('%Y-%m-%d')}
    daily_data["location"] = [city_info["city"]] * len(date_range)
    daily_data["weather_code"] = daily.Variables(0).ValuesAsNumpy()
    daily_data["temperature_2m_max"] = daily.Variables(1).ValuesAsNumpy()
    daily_data["temperature_2m_min"] = daily.Variables(2).ValuesAsNumpy()
    daily_data["temperature_2m_mean"] = daily.Variables(3).ValuesAsNumpy()
    daily_data["apparent_temperature_max"] = daily.Variables(4).ValuesAsNumpy()
    daily_data["apparent_temperature_min"] = daily.Variables(5).ValuesAsNumpy()
    daily_data["apparent_temperature_mean"] = daily.Variables(6).ValuesAsNumpy()
    daily_data["sunrise"] = pd.to_datetime(daily.Variables(7).ValuesAsNumpy(), unit='s').strftime('%H:%M:%S')
    daily_data["sunset"] = pd.to_datetime(daily.Variables(8).ValuesAsNumpy(), unit='s').strftime('%H:%M:%S')
    daily_data["daylight_duration"] = daily.Variables(9).ValuesAsNumpy()
    daily_data["sunshine_duration"] = daily.Variables(10).ValuesAsNumpy()
    daily_data["precipitation_sum"] = daily.Variables(11).ValuesAsNumpy()
    daily_data["rain_sum"] = daily.Variables(12).ValuesAsNumpy()
    daily_data["snowfall_sum"] = daily.Variables(13).ValuesAsNumpy()
    daily_data["precipitation_hours"] = daily.Variables(14).ValuesAsNumpy()
    daily_data["wind_speed_10m_max"] = daily.Variables(15).ValuesAsNumpy()
    daily_data["wind_gusts_10m_max"] = daily.Variables(16).ValuesAsNumpy()
    daily_data["wind_direction_10m_dominant"] = daily.Variables(17).ValuesAsNumpy()
    daily_data["et0_fao_evapotranspiration"] = daily.Variables(18).ValuesAsNumpy()

    daily_dataframe = pd.DataFrame(data=daily_data)
    country_dir = os.path.join(base_dir, city_info["country"])
    os.makedirs(country_dir, exist_ok=True)
    file_path = os.path.join(country_dir, f'{city_info["city"]}_weather_daily_api.jsonl')
    daily_dataframe.to_json(file_path, orient='records', lines=True)
    print(f'Data saved to {file_path}')

# Function to fetch and save hourly weather data
def fetch_and_save_hourly_weather(city_info):
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": city_info["latitude"],
        "longitude": city_info["longitude"],
        "start_date": "2014-07-09",
        "end_date": "2024-07-11",
        "hourly": ["temperature_2m", "dew_point_2m", "precipitation", "rain", "snowfall", "snow_depth", "pressure_msl",
                   "surface_pressure", "cloud_cover", "et0_fao_evapotranspiration", "wind_speed_10m", "wind_direction_10m",
                   "wind_gusts_10m"],
        "timezone": "auto"
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process response data
    response = responses[0]
    hourly = response.Hourly()
    date_range = pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
    formatted_dates = date_range.strftime('%Y-%m-%d %H:%M:%S')
    location = [city_info["city"]] * len(formatted_dates)
    hourly_data = {
        "date": formatted_dates,
        "location": location,
        "temperature_2m": hourly.Variables(0).ValuesAsNumpy(),
        "dew_point_2m": hourly.Variables(1).ValuesAsNumpy(),
        "precipitation": hourly.Variables(2).ValuesAsNumpy(),
        "rain": hourly.Variables(3).ValuesAsNumpy(),
        "snowfall": hourly.Variables(4).ValuesAsNumpy(),
        "snow_depth": hourly.Variables(5).ValuesAsNumpy(),
        "pressure_msl": hourly.Variables(6).ValuesAsNumpy(),
        "surface_pressure": hourly.Variables(7).ValuesAsNumpy(),
        "cloud_cover": hourly.Variables(8).ValuesAsNumpy(),
        "et0_fao_evapotranspiration": hourly.Variables(9).ValuesAsNumpy(),
        "wind_speed_10m": hourly.Variables(10).ValuesAsNumpy(),
        "wind_direction_10m": hourly.Variables(11).ValuesAsNumpy(),
        "wind_gusts_10m": hourly.Variables(12).ValuesAsNumpy()
    }

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    country_dir = os.path.join(base_dir, city_info["country"])
    os.makedirs(country_dir, exist_ok=True)
    file_path = os.path.join(country_dir, f'{city_info["city"]}_weather_hourly_api.jsonl')
    hourly_dataframe.to_json(file_path, orient='records', lines=True)
    print(f'Data saved to {file_path}')

# Loop through cities and fetch weather data
for city_info in cities:
    fetch_and_save_daily_weather(city_info)
    fetch_and_save_hourly_weather(city_info)
    print(f"Next fetch in 60 seconds for {city_info['city']} in {city_info['country']}")
    for remaining in range(60, 0, -1):
        sys.stdout.write("\r")
        sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    print("\n")
