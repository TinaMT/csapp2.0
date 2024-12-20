import os
import logging
from utils.api_utils import APIBase

class queryROAMWStatusAPIs(APIBase):
    def __init__(self, session):
        super().__init__(session)
    
    def get_params_info(self, params):
        url = f"{os.getenv('API_SERVER')}/cs/API/queryROAMWStatus"

        # 請求
        self.api_request("get", url, params=params)
        logging.info(f"Generated URL: {url}")

        return self.response