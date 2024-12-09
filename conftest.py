import os
from dotenv import load_dotenv

def load_environment():
    # 檢查是否設置了 ENV_FILE 環境變數
    env_file = os.environ.get('ENV_FILE')
    
    if env_file:
        # 如果設置了，則加載指定的 .env 文件
        load_dotenv(env_file)
        print(f"Loaded environment from {env_file}")
    else:
        # 否則加載默認的 .env 文件
        load_dotenv()
        print("Loaded default .env file")

load_environment()
