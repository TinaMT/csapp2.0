import pytest
import logging
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning   #SSL
from test_data.get_data_from_excel import process_data
from api_objects.CustomerInfoAPIs import CustomerInfoAPIs
from utils.object_utils import ObjectUtils


# 屏蔽 InsecureRequestWarning 警告
urllib3.disable_warnings(InsecureRequestWarning)

# #讀取Excel 
file_path = 'test_data/AllAPIs.xlsx'
name = 'CustomerInfoAPIs'
data_process = process_data(file_path, name)

@pytest.mark.parametrize('data_dict',data_process)  #'data_dict'尋找body裡面
def test_CustomerInfoAPIs(data_dict,get_session):
    #工作表裡的標頭
    requests_params = data_dict['params']
    excel_result = data_dict['Expected Result']
    
    try:
        #呼叫API
        call_api = CustomerInfoAPIs(get_session)

        # 記錄發送的請求參數
        logging.info(f"Sending API request with parameters:\n{requests_params}\n")
     
        #回傳結果
        requests_params = json.loads(requests_params)
        response = call_api.get_params_info(requests_params)

        #判斷狀態碼
        if response.status_code != 200:
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")
            assert response.status_code == 200,f"Failed to retrieve data. Status code: {response.status_code}"
            return
        

        #sort_keys=True 避免受順序影響
        response_data = json.dumps(response.text, sort_keys=True)
        excel_data = json.dumps(excel_result, sort_keys=True)


        # 比較是否相等
        if response_data != excel_data:
            logging.error(f"[資料比對失敗:],\n expected: {json.dumps(excel_data)}, \n but actual: {json.dumps(response_data)}")
            assert ObjectUtils.equal_str("資料比對失敗", excel_data , response_data)
        



    except Exception as e:
        logging.exception(f'error：{e}')
        raise
    finally:
        # 從 data_dict 中提取測試編號
        test_number = data_dict.get('No', 'Unknown')
        logging.info(f'Test {test_number} END \n================================================================================================================================')