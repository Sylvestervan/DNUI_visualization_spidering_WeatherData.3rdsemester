import json
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 数据库连接设置
user = 'root'
password = 'fjd2023dnui'
host = 'localhost'
database = 'WeatherBroadcastSystem'

# 创建数据库引擎
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# 创建一个会话类
Session = sessionmaker(bind=engine)
session = Session()

# 读取jsonl文件并转换为DataFrame
def read_jsonl_to_df(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            data.append(json.loads(line))
    return pd.DataFrame(data)

# 读取数据文件
daily_file_path = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Combinations/EU/eu_daily_weather.jsonl'
hourly_file_path = '/Users/fanjindong/Desktop/Semester-3/Submission/main/weather_data_collections/Combinations/EU/eu_hourly_weather.jsonl'

daily_df = read_jsonl_to_df(daily_file_path)
hourly_df = read_jsonl_to_df(hourly_file_path)

# 存储到数据库
def store_to_db(df, table_name, engine, session):
    try:
        # 启动事务
        with engine.begin() as connection:
            df.to_sql(name=table_name, con=connection, if_exists='append', index=False)
        # 提交事务
        session.commit()
    except Exception as e:
        # 回滚事务
        session.rollback()
        print(f"Error occurred: {e}")
        raise

# 存储数据到数据库表weather_data_by_api
try:
    store_to_db(daily_df, 'eu_daily_weather_data_by_api', engine, session)
    store_to_db(hourly_df, 'eu_hourly_weather_data_by_api', engine, session)
except Exception as e:
    print("Transaction failed and rolled back.")
finally:
    session.close()
