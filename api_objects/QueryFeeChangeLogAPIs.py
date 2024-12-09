# [014]查詢變更資費紀錄API

import os
from utils.api_utils import APIBase

class queryFeeChangeLogAPIs(APIBase):

    def __init__(self, session):
        super().__init__(session)
    
    def get_data_info(self, params):

        url = f"{os.getenv('API_SERVER')}/cs/API/queryFeeChangeLog"

        self.api_request("get", url, params=params)

        return self.response
    