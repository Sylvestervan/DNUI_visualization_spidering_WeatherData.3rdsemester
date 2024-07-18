import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy.optimize import curve_fit
import streamlit as st
import json
import matplotlib.dates as mdates

# Load the data
file_path = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_Spider/cn/qiqihar_weather_daily.jsonl'  # 请确保这个文件路径正确
data = []
with open(file_path, 'r') as file:
    for line in file:
        data.append(json.loads(line))

df = pd.DataFrame(data)

# Convert time to hours in decimal format
def time_to_hours(time_str):
    try:
        dt = datetime.strptime(time_str, '%I:%M %p')
        return dt.hour + dt.minute / 60
    except ValueError:
        return None

df['sunrise_hours'] = df['sunrise'].apply(time_to_hours)
df['sunset_hours'] = df['sunset'].apply(time_to_hours)
df['moonrise_hours'] = df['moonrise'].apply(time_to_hours)
df['moonset_hours'] = df['moonset'].apply(time_to_hours)
df = df.dropna(subset=['moonrise_hours', 'moonset_hours'])

# Define the sine function to fit
def sine_function(x, A, B, C, D):
    return A * np.sin(B * x + C) + D

# Select a subset of data for faster computation
df_subset = df.iloc[::7]  # Use every 7th row
x_data = np.arange(len(df_subset))

# Fit sine function to sunrise data
sunrise_params, _ = curve_fit(sine_function, x_data, df_subset['sunrise_hours'])
sunrise_fit = sine_function(x_data, *sunrise_params)

# Fit sine function to sunset data
sunset_params, _ = curve_fit(sine_function, x_data, df_subset['sunset_hours'])
sunset_fit = sine_function(x_data, *sunset_params)

# Fit sine function to moonrise data
moonrise_params, _ = curve_fit(sine_function, x_data, df_subset['moonrise_hours'])
moonrise_fit = sine_function(x_data, *moonrise_params)

# Fit sine function to moonset data
moonset_params, _ = curve_fit(sine_function, x_data, df_subset['moonset_hours'])
moonset_fit = sine_function(x_data, *moonset_params)

# Streamlit app layout
st.title("Sunrise and Sunset Times in Qiqihar")
st.write("## Fitted Curves")

# Plot sunrise and sunset times with fitted curves
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(df_subset['date'], df_subset['sunrise_hours'], label='Sunrise Time', marker='o')
ax.plot(df_subset['date'], sunrise_fit, label='Fitted Sunrise Curve', linestyle='--')
ax.plot(df_subset['date'], df_subset['sunset_hours'], label='Sunset Time', marker='o')
ax.plot(df_subset['date'], sunset_fit, label='Fitted Sunset Curve', linestyle='--')
ax.set_xlabel('Date')
ax.set_ylabel('Time (hours)')
ax.set_title('Sunrise and Sunset Times in Qiqihar with Fitted Curves')
ax.legend()
ax.grid(True)
# Simplify date labels
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()
st.pyplot(fig)

st.write("## Moonrise and Moonset Times in Qiqihar")

# Plot moonrise and moonset times with fitted curves
fig, ax = plt.subplots(figsize=(14, 7))
ax.plot(df_subset['date'], df_subset['moonrise_hours'], label='Moonrise Time', marker='o')
ax.plot(df_subset['date'], moonrise_fit, label='Fitted Moonrise Curve', linestyle='--')
ax.plot(df_subset['date'], df_subset['moonset_hours'], label='Moonset Time', marker='o')
ax.plot(df_subset['date'], moonset_fit, label='Fitted Moonset Curve', linestyle='--')
ax.set_xlabel('Date')
ax.set_ylabel('Time (hours)')
ax.set_title('Moonrise and Moonset Times in Qiqihar with Fitted Curves')
ax.legend()
ax.grid(True)
# Simplify date labels
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
fig.autofmt_xdate()
st.pyplot(fig)

st.write("## Fitted Parameters")
st.write("### Sunrise Parameters")
st.write(sunrise_params)
st.write("### Sunset Parameters")
st.write(sunset_params)
st.write("### Moonrise Parameters")
st.write(moonrise_params)
st.write("### Moonset Parameters")
st.write(moonset_params)
