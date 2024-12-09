import pytest
import logging
import json
import urllib3
from urllib3.exceptions import InsecureRequestWarning   
from test_data.get_data_from_excel import process_data
from api_objects.ModifyBaseServiceAPIs import modifyBaseServiceAPIs
from utils.object_utils import ObjectUtils


urllib3.disable_warnings(InsecureRequestWarning)

 
file_path = 'test_data/AllAPIs.xlsx'
name = 'ModifyBaseServiceAPIs'
data_process = process_data(file_path, name)

@pytest.mark.parametrize('data_dict',data_process)  
def test_CustomerInfoAPIs(data_dict,get_session):
   
    requests_params = data_dict['params']
    excel_result = data_dict['Expected Result']
    
    try:
        
        call_api = modifyBaseServiceAPIs(get_session)

        
        logging.info(f"Sending API request with parameters:\n{requests_params}\n")
     
        
        requests_params = json.loads(requests_params)
        response = call_api.get_params_info(requests_params)

        
        if response.status_code != 200:
            logging.error(f"Failed to retrieve data. Status code: {response.status_code}")
            assert response.status_code == 200,f"Failed to retrieve data. Status code: {response.status_code}"
            return
        

        
        response_data = json.dumps(response.text, sort_keys=True)
        excel_data = json.dumps(excel_result, sort_keys=True)

        
        if response_data != excel_data:
            logging.error(f"[資料比對失敗:],\n expected: {json.dumps(excel_data)}, \n but actual: {json.dumps(response_data)}")
            assert ObjectUtils.equal_str("資料比對失敗", excel_data , response_data)
        
    except Exception as e:
        logging.exception(f'error：{e}')
        raise
    finally:
       
        test_number = data_dict.get('No', 'Unknown')
        logging.info(f'Test {test_number} END \n================================================================================================================================')