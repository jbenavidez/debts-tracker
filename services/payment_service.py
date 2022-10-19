from typing import Dict, List
from .utility import UtilityService
import requests
import traceback

class PaymentService:
    """
    This services is use to get data from the payment API and all the logic relate to payment
    """
    logger = UtilityService.get_logger(__name__)
    url = "https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payments"
    unvalid_debts_record = [] # will contains debts that could not be validate by our validators

    @classmethod 
    def fetch_payment_from_api(cls) -> List[Dict]:
        # this is used fetch list of payment_plans from api
        try:
            response  = requests.get(cls.url)
            cls.logger.info(f"Payment API call succefully {response.status_code}")
        except Exception as e:
            cls.logger.error(f"Payment API Call Failed {e},Error line {traceback.format_exc()}")
            
        # Important keys
        # - payment_plan_id
        # - amount 
        # - date   
        return response.json()
    
    @classmethod 
    def get_payments(cls) -> Dict:
        # this function is used to validate data and convert list to dict (dicts are faster for data retrieve)
        debts = cls.fetch_payment_from_api()
        debts_dict = {}
        for item in debts:
            try:
                payment_plan_id = item["payment_plan_id"]
                UtilityService.payment_validator(item) #valdiate payment
                cls.logger.info(f"validated payment info {payment_plan_id}")
                if debts_dict.get(payment_plan_id) is None:
                    debts_dict[payment_plan_id] = [item]
                else:
                    debts_dict[payment_plan_id].append(item)
            except Exception as e:
                cls.logger.error(f"Could not validate payment {e},Error line {traceback.format_exc()}")
                cls.unvalid_debts_record.append(item)
         # Important keys
        # - K: payment_plan_id
        # - V: payments values     
        return debts_dict
            
        
