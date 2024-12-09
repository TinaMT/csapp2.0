# [130]電子簡訊帳單查詢

import os
from utils.api_utils import APIBase

class ebillListIIIAPIs(APIBase):

    def __init__(self, session):
        super().__init__(session)
    
    def get_data_info(self, params):

        url = f"{os.getenv('API_SERVER')}/cs/API/ebillListIII"

        self.api_request("get", url, params=params)

        return self.response
    