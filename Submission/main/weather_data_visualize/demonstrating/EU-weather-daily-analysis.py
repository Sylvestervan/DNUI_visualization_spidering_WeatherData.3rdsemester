import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import folium
from streamlit_folium import folium_static

# 城市和经纬度数据
city_coords = {
    "london": {"latitude": 51.5074, "longitude": -0.1278},
    "manchester": {"latitude": 53.4808, "longitude": -2.2426},
    "edinburgh": {"latitude": 55.9533, "longitude": -3.1883},
    "paris": {"latitude": 48.8566, "longitude": 2.3522},
    "marseille": {"latitude": 43.2965, "longitude": 5.3698},
    "nice": {"latitude": 43.7102, "longitude": 7.2620},
    "berlin": {"latitude": 52.5200, "longitude": 13.4050},
    "hamburg": {"latitude": 53.5511, "longitude": 9.9937},
    "munich": {"latitude": 48.1351, "longitude": 11.5820},
    "rome": {"latitude": 41.9028, "longitude": 12.4964},
    "milan": {"latitude": 45.4642, "longitude": 9.1900},
    "naples": {"latitude": 40.8518, "longitude": 14.2681},
    "madrid": {"latitude": 40.4168, "longitude": -3.7038},
    "barcelona": {"latitude": 41.3851, "longitude": 2.1734},
    "valencia": {"latitude": 39.4699, "longitude": -0.3763},
    "amsterdam": {"latitude": 52.3676, "longitude": 4.9041},
    "rotterdam": {"latitude": 51.9225, "longitude": 4.4791},
    "zurich": {"latitude": 47.3769, "longitude": 8.5417},
    "geneva": {"latitude": 46.2044, "longitude": 6.1432},
    "stockholm": {"latitude": 59.3293, "longitude": 18.0686},
    "gothenburg": {"latitude": 57.7089, "longitude": 11.9746},
    "oslo": {"latitude": 59.9139, "longitude": 10.7522},
    "bergen": {"latitude": 60.3913, "longitude": 5.3221},
    "copenhagen": {"latitude": 55.6761, "longitude": 12.5683},
    "vienna": {"latitude": 48.2082, "longitude": 16.3738},
    "brussels": {"latitude": 50.8503, "longitude": 4.3517},
    "dublin": {"latitude": 53.3498, "longitude": -6.2603},
    "helsinki": {"latitude": 60.1699, "longitude": 24.9384},
    "athens": {"latitude": 37.9838, "longitude": 23.7275},
    "warsaw": {"latitude": 52.2297, "longitude": 21.0122},
    "lisbon": {"latitude": 38.7169, "longitude": -9.1399},
    "prague": {"latitude": 50.0755, "longitude": 14.4378},
    "budapest": {"latitude": 47.4979, "longitude": 19.0402},
    "bucharest": {"latitude": 44.4268, "longitude": 26.1025},
    "zagreb": {"latitude": 45.8150, "longitude": 15.9819},
    "moscow": {"latitude": 55.7558, "longitude": 37.6173},
    "saint_petersburg": {"latitude": 59.9343, "longitude": 30.3351},
    "nicosia": {"latitude": 35.1856, "longitude": 33.3823},
    "reykjavik": {"latitude": 64.1355, "longitude": -21.8954},
    "ljubljana": {"latitude": 46.0569, "longitude": 14.5058},
    "sofia": {"latitude": 42.6977, "longitude": 23.3219},
    "bratislava": {"latitude": 48.1486, "longitude": 17.1077},
    "kyiv": {"latitude": 50.4501, "longitude": 30.5234},
    "minsk": {"latitude": 53.9045, "longitude": 27.5615}
}

# 加载所有城市数据
file_path = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Combinations/EU/eu_daily_weather.jsonl'


@st.cache_data
def load_all_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return pd.DataFrame(data)


# 加载数据
data = load_all_data(file_path)

# 检查数据结构
st.write(data.head())
st.write(data.columns)


def visualize_weather(city_names, data):
    # 地图可视化
    m = folium.Map(location=[50, 10], zoom_start=4)

    for city_name in city_names:
        city_data = data[data['location'] == city_name]

        # 获取城市坐标
        latitude = city_coords[city_name.lower()]['latitude']
        longitude = city_coords[city_name.lower()]['longitude']

        # 计算气候统计信息
        min_temp = city_data['temperature_2m_min'].min()
        max_temp = city_data['temperature_2m_max'].max()
        avg_sunshine = city_data['sunshine_duration'].mean() / 60  # 转换为分钟
        avg_precipitation = city_data['precipitation_sum'].mean()  # 平均降水量 (mm)

        # 创建信息字符串
        info = f"In Past 10 yrs, Min Temp: {min_temp}°C\nMax Temp: {max_temp}°C\nAvg Sunshine: {avg_sunshine:.2f} mins/day\nAvg Precipitation: {avg_precipitation:.2f} m/year"

        # 添加标记到地图
        folium.Marker(
            [latitude, longitude],
            popup=folium.Popup(info, max_width=300),
            tooltip=city_name
        ).add_to(m)

    # 显示地图
    folium_static(m)

    # 每日温度趋势对比
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        city_data = data[data['location'] == city_name]

        # 解析日期列
        city_data['date'] = pd.to_datetime(city_data['date'])
        city_data.set_index('date', inplace=True)

        # 提取每日温度数据
        temperature = city_data['temperature_2m_mean'].dropna()

        # 可视化每日温度趋势
        sns.lineplot(data=city_data, x=city_data.index, y='temperature_2m_mean', label=f'{city_name} Daily Avg Temp',
                     linewidth=1)

    plt.title('Daily Temperature Trend Comparison', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine()
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

    # 傅里叶变换对比
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        city_data = data[data['location'] == city_name]
        city_data['date'] = pd.to_datetime(city_data['date'])
        city_data.set_index('date', inplace=True)
        temperature = city_data['temperature_2m_mean'].dropna()

        temperature_fft = np.fft.fft(temperature)
        fft_freqs = np.fft.fftfreq(len(temperature))

        # 排除零频率成分，并聚焦于低频部分
        positive_freqs = (fft_freqs > 0) & (fft_freqs < 0.1)
        freq_range = fft_freqs[positive_freqs]
        amplitude_range = np.abs(temperature_fft)[positive_freqs]

        plt.plot(freq_range, amplitude_range, linewidth=1, label=f'{city_name}')

    plt.title('Fourier Transform of Temperature Data Comparison (Zoomed In)', fontsize=16, fontweight='bold')
    plt.xlabel('Frequency', fontsize=14)
    plt.ylabel('Amplitude', fontsize=14)
    plt.yscale('log')
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

    # 逐年变化对比
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        city_data = data[data['location'] == city_name]
        city_data['date'] = pd.to_datetime(city_data['date'])
        city_data.set_index('date', inplace=True)
        city_data['year'] = city_data.index.year
        yearly_temp = city_data.groupby('year')['temperature_2m_mean'].mean()

        sns.lineplot(data=yearly_temp, marker='o', linewidth=2, label=f'{city_name}')

    plt.title('Yearly Average Temperature Change Comparison', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Temperature (°C)', fontsize=14)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine()
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()

    # 多项式回归分析
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        city_data = data[data['location'] == city_name]
        city_data['date'] = pd.to_datetime(city_data['date'])
        city_data.set_index('date', inplace=True)
        temperature = city_data['temperature_2m_mean'].dropna()

        # 多项式回归分析
        z = np.polyfit(range(len(temperature)), temperature.values, 4)
        p = np.poly1d(z)
        plt.plot(temperature.index, p(range(len(temperature))), linestyle='--', label=f'{city_name} Polynomial Fit')

    plt.title('Polynomial Regression Analysis of Temperature Data', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.legend(fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine()
    plt.tight_layout()
    st.pyplot(plt)
    plt.clf()


# Streamlit应用标题
st.title('European Weather Visualization')

# 选择城市
available_cities = data['location'].unique().tolist()
selected_cities = st.multiselect('Select cities to compare:', available_cities, default=available_cities[:5])

# 可视化天气数据
if st.button('Visualize'):
    visualize_weather(selected_cities, data)
