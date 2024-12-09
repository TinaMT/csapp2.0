# [131]電子簡訊帳單申請/異動/取消

import os
from utils.api_utils import APIBase


class ebillActionIIIAPIs(APIBase):

    def __init__(self, session):
        super().__init__(session)
    
    def get_data_info(self, params):

        url = f"{os.getenv('API_SERVER')}/cs/API/ebillActionIII"

        self.api_request("get", url, params=params)

        return self.response
    