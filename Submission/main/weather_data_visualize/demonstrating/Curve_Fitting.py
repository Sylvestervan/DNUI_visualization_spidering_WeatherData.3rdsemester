import pandas as pd
import numpy as np
from datetime import datetime
from scipy.optimize import curve_fit
import streamlit as st
import json
import plotly.graph_objects as go

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

# Convert dates to datetime
df_subset['date'] = pd.to_datetime(df_subset['date'])

# Streamlit app layout
st.title("Sunrise and Sunset Times in Qiqihar")
st.write("## Fitted Curves")

# Plot sunrise and sunset times with fitted curves using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_subset['date'], y=df_subset['sunrise_hours'], mode='markers', name='Sunrise Time'))
fig.add_trace(go.Scatter(x=df_subset['date'], y=sunrise_fit, mode='lines', name='Fitted Sunrise Curve'))
fig.add_trace(go.Scatter(x=df_subset['date'], y=df_subset['sunset_hours'], mode='markers', name='Sunset Time'))
fig.add_trace(go.Scatter(x=df_subset['date'], y=sunset_fit, mode='lines', name='Fitted Sunset Curve'))
fig.update_layout(title='Sunrise and Sunset Times in Qiqihar with Fitted Curves',
                  xaxis_title='Date',
                  yaxis_title='Time (hours)',
                  xaxis=dict(tickformat='%Y-%m-%d'))
st.plotly_chart(fig)

st.write("## Moonrise and Moonset Times in Qiqihar")

# Plot moonrise and moonset times with fitted curves using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=df_subset['date'], y=df_subset['moonrise_hours'], mode='markers', name='Moonrise Time'))
fig.add_trace(go.Scatter(x=df_subset['date'], y=moonrise_fit, mode='lines', name='Fitted Moonrise Curve'))
fig.add_trace(go.Scatter(x=df_subset['date'], y=df_subset['moonset_hours'], mode='markers', name='Moonset Time'))
fig.add_trace(go.Scatter(x=df_subset['date'], y=moonset_fit, mode='lines', name='Fitted Moonset Curve'))
fig.update_layout(title='Moonrise and Moonset Times in Qiqihar with Fitted Curves',
                  xaxis_title='Date',
                  yaxis_title='Time (hours)',
                  xaxis=dict(tickformat='%Y-%m-%d'))
st.plotly_chart(fig)

st.write("## Fitted Parameters")
st.write("### Sunrise Parameters")
st.write(sunrise_params)
st.write("### Sunset Parameters")
st.write(sunset_params)
st.write("### Moonrise Parameters")
st.write(moonrise_params)
st.write("### Moonset Parameters")
st.write(moonset_params)
