import os

# 定义根目录
root_dir = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Collection_of_API/'

# 定义输出文件路径
daily_output_file = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Combinations/EU/eu_daily_weather.jsonl'
hourly_output_file = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Combinations/EU/eu_hourly_weather.jsonl'

# 函数：合并JSONL文件
def merge_jsonl_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                for line in infile:
                    outfile.write(line)

# 收集所有每日和每小时的文件路径
daily_files = []
hourly_files = []

for country_dir in os.listdir(root_dir):
    country_path = os.path.join(root_dir, country_dir)
    if os.path.isdir(country_path):
        for file_name in os.listdir(country_path):
            if 'daily' in file_name:
                daily_files.append(os.path.join(country_path, file_name))
            elif 'hourly' in file_name:
                hourly_files.append(os.path.join(country_path, file_name))

# 合并所有每日文件
merge_jsonl_files(daily_files, daily_output_file)
print(f'Merged daily files into {daily_output_file}')

# 合并所有每小时文件
merge_jsonl_files(hourly_files, hourly_output_file)
print(f'Merged hourly files into {hourly_output_file}')
