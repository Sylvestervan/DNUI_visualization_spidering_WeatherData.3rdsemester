import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# 设置Seaborn样式
sns.set(style="whitegrid", palette="muted", color_codes=True)

# 定义数据文件路径
data_files = {
    'Stockholm': '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/sweden/stockholm_weather_daily_api.jsonl',
    'Oslo': '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/norway/oslo_weather_daily_api.jsonl',
    'Saint-Petersburg': '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/russia/saint_petersburg_weather_daily_api.jsonl',
    'Helsinki': '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/finland/helsinki_weather_daily_api.jsonl',
    'Reykjavik': '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/iceland/reykjavik_weather_daily_api.jsonl',
    'Bergen': '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/norway/bergen_weather_daily_api.jsonl'
}


@st.cache_data
def load_data(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    return data


def visualize_weather(city_names):
    # 每日温度趋势对比
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        daily_data = load_data(data_files[city_name])

        # 转换数据为 DataFrame
        daily_df = pd.DataFrame(daily_data)

        # 解析日期列
        daily_df['date'] = pd.to_datetime(daily_df['date'])
        daily_df.set_index('date', inplace=True)

        # 提取每日温度数据
        temperature = daily_df['temperature_2m_mean'].dropna()

        # 可视化每日温度趋势
        sns.lineplot(data=daily_df, x=daily_df.index, y='temperature_2m_mean',
                     label=f'{city_name} Daily Average Temperature', linewidth=1)

    plt.title('Daily Temperature Trend Comparison: West and North Europe', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Temperature (°C)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine()
    plt.tight_layout()
    st.pyplot(plt)

    # 傅里叶变换对比
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        daily_data = load_data(data_files[city_name])
        daily_df = pd.DataFrame(daily_data)
        daily_df['date'] = pd.to_datetime(daily_df['date'])
        daily_df.set_index('date', inplace=True)
        temperature = daily_df['temperature_2m_mean'].dropna()

        temperature_fft = np.fft.fft(temperature)
        fft_freqs = np.fft.fftfreq(len(temperature))

        # 排除零频率成分，并聚焦于低频部分
        positive_freqs = (fft_freqs > 0) & (fft_freqs < 0.1)  # 仅展示频率在0.1以下的部分
        freq_range = fft_freqs[positive_freqs]
        amplitude_range = np.abs(temperature_fft)[positive_freqs]

        plt.plot(freq_range, amplitude_range, linewidth=1, label=f'{city_name}')

    plt.title('Fourier Transform of Temperature Data Comparison: West and North Europe (Zoomed In)', fontsize=16, fontweight='bold')
    plt.xlabel('Frequency', fontsize=14)
    plt.ylabel('Amplitude', fontsize=14)
    plt.yscale('log')  # 使用对数坐标
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    st.pyplot(plt)

    # 逐年变化对比
    plt.figure(figsize=(14, 7))
    for city_name in city_names:
        daily_data = load_data(data_files[city_name])
        daily_df = pd.DataFrame(daily_data)
        daily_df['date'] = pd.to_datetime(daily_df['date'])
        daily_df.set_index('date', inplace=True)
        daily_df['year'] = daily_df.index.year
        yearly_temp = daily_df.groupby('year')['temperature_2m_mean'].mean()

        sns.lineplot(data=yearly_temp, marker='o', linewidth=2, label=f'{city_name}')

    plt.title('Yearly Average Temperature Change Comparison: West and North Europe', fontsize=16, fontweight='bold')
    plt.xlabel('Year', fontsize=14)
    plt.ylabel('Average Temperature (°C)', fontsize=14)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    sns.despine()
    plt.tight_layout()
    st.pyplot(plt)


# Streamlit应用标题
st.title('Weather Visualization in europe at 60 latitude')

# 选择城市
selected_cities = st.multiselect('Select cities to compare:', list(data_files.keys()),
                                 default=['Stockholm', 'Oslo', 'Saint-Petersburg', 'Helsinki', 'Reykjavik', 'Bergen'])

# 可视化天气数据
if st.button('Visualize'):
    visualize_weather(selected_cities)
