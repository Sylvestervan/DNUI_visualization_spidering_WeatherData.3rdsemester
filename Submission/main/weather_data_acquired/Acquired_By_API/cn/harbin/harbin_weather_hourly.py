import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

city = 'harbin'

# Set up the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=-1)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 45.75,
    "longitude": 126.65,
    "start_date": "2014-07-09",
    "end_date": "2024-07-11",
    "hourly": ["temperature_2m", "dew_point_2m", "precipitation", "rain", "snowfall", "snow_depth", "pressure_msl",
               "surface_pressure", "cloud_cover", "et0_fao_evapotranspiration", "wind_speed_10m", "wind_direction_10m",
               "wind_gusts_10m"],
    "timezone": "auto"
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process hourly data. The order of variables needs to be the same as requested.
hourly = response.Hourly()
hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
hourly_dew_point_2m = hourly.Variables(1).ValuesAsNumpy()
hourly_precipitation = hourly.Variables(2).ValuesAsNumpy()
hourly_rain = hourly.Variables(3).ValuesAsNumpy()
hourly_snowfall = hourly.Variables(4).ValuesAsNumpy()
hourly_snow_depth = hourly.Variables(5).ValuesAsNumpy()
hourly_pressure_msl = hourly.Variables(6).ValuesAsNumpy()
hourly_surface_pressure = hourly.Variables(7).ValuesAsNumpy()
hourly_cloud_cover = hourly.Variables(8).ValuesAsNumpy()
hourly_et0_fao_evapotranspiration = hourly.Variables(9).ValuesAsNumpy()
hourly_wind_speed_10m = hourly.Variables(10).ValuesAsNumpy()
hourly_wind_direction_10m = hourly.Variables(11).ValuesAsNumpy()
hourly_wind_gusts_10m = hourly.Variables(12).ValuesAsNumpy()

# Convert timestamps to datetime
date_range = pd.date_range(
    start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
    end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
    freq=pd.Timedelta(seconds=hourly.Interval()),
    inclusive="left"
)

# Format date to yyyy-mm-dd HH:MM:SS
formatted_dates = date_range.strftime('%Y-%m-%d %H:%M:%S')

# Add location field
location = [f"{city}"] * len(formatted_dates)

hourly_data = {
    "date": formatted_dates,
    "location": location,
    "temperature_2m": hourly_temperature_2m,
    "dew_point_2m": hourly_dew_point_2m,
    "precipitation": hourly_precipitation,
    "rain": hourly_rain,
    "snowfall": hourly_snowfall,
    "snow_depth": hourly_snow_depth,
    "pressure_msl": hourly_pressure_msl,
    "surface_pressure": hourly_surface_pressure,
    "cloud_cover": hourly_cloud_cover,
    "et0_fao_evapotranspiration": hourly_et0_fao_evapotranspiration,
    "wind_speed_10m": hourly_wind_speed_10m,
    "wind_direction_10m": hourly_wind_direction_10m,
    "wind_gusts_10m": hourly_wind_gusts_10m
}

hourly_dataframe = pd.DataFrame(data=hourly_data)
print(hourly_dataframe)

# Specify file path
file_path = f'/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/cn/{city}_weather_hourly_api.jsonl'

# Save DataFrame as JSONL file
hourly_dataframe.to_json(file_path, orient='records', lines=True)

print(f'Data saved to {file_path}')
