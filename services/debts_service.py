from typing import Dict, List
from .utility import UtilityService
import requests
import traceback

class DebtsService:
    """
    this services is uses to debts info from the API
    """
    logger = UtilityService.get_logger(__name__)
    url = "https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/debts"
    invalid_debts_record = [] # will contains debts that could not be validate by our validor

    @classmethod 
    def fetch_debts_from_api(cls) -> List[Dict]:
        # this is used fetch list of debt from api
        try:
            response  = requests.get(cls.url)
            cls.logger.info(f"Debts API call succefully {response.status_code}")
        except Exception as e:
            cls.logger.error(f"Debts API Call Failed {e},Error line {traceback.format_exc()}")
            
        # Important keys
        # - id
        # - amount
        return response.json()
    
    @classmethod 
    def get_debts(cls) -> Dict:
        # this function is used to validate data and convert list to dict (dicts are faster for data retrieve)
        debts = cls.fetch_debts_from_api()
        debts_dict = {}
        for item in debts:
            try:
                debt_id = item["id"]
                UtilityService.debts_validator(item) #valdiate debts
                cls.logger.info(f"validated Debts info {debt_id}")
                if debts_dict.get(debt_id) is None:
                    debts_dict[debt_id] = item
            except Exception as e:
                cls.logger.error(f"Could not validate debt {e},Error line {traceback.format_exc()}")
                cls.invalid_debts_record.append(item)
         # Important keys
        # - K: debt_id
        # - V: debts values       
        return debts_dict
            
        
