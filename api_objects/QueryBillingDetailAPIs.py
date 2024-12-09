# [056]本期帳單明細查詢API

import os
from utils.api_utils import APIBase

class queryBillingDetailAPIs(APIBase):

    def __init__(self, session):
        super().__init__(session)
    
    def get_data_info(self, params):

        url = f"{os.getenv('API_SERVER')}/cs/API/queryBillingDetail"

        self.api_request("get", url, params=params)

        return self.response
    