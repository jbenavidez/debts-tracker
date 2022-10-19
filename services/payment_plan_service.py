from typing import Dict, List
from .utility import UtilityService
import requests
import traceback

class PaymentPlanService:
    """
    This services is use to get data from the payment API and all the logic relate to payment plan
    """
    logger = UtilityService.get_logger(__name__)
    url = "https://my-json-server.typicode.com/druska/trueaccord-mock-payments-api/payment_plans"
    invalid_payments = [] # will contains payment that could not be validate by our validators

    @classmethod 
    def fetch_payment_plan_from_api(cls) -> List[Dict]:
        # this is used fetch list of payment from api
        try:
            response  = requests.get(cls.url)
            cls.logger.info(f"Payment Plans API call succefully {response.status_code}")
        except Exception as e:
            cls.logger.error(f"Payment Plans  API Call Failed {e},Error line {traceback.format_exc()}")
            
        # Important keys
        # - id
        # - debt_id 
        # - amount_to_pay
        # - installment_amount 
        # - installment_frequency
        # - start_date        
        return response.json()
    
    @classmethod 
    def get_payment_plans(cls) -> Dict:
        # this function is used to validate data and convert list to dict (dicts are faster for data retrieve)
        debts = cls.fetch_payment_plan_from_api()
        debts_dict = {}
        for item in debts:
            try:
                debt_id = item["debt_id"]
                UtilityService.payment_plan_validator(item) #valdiate payment_plans
                cls.logger.info(f"validated payment_plan info {debt_id}")
                if debts_dict.get(debt_id) is None:
                    debts_dict[debt_id] = item

            except Exception as e:
                cls.logger.error(f"Could not validate payment_plan {e},Error line {traceback.format_exc()}")
                cls.invalid_payments.append(item)
         # Important keys
        # - K: debt_id
        # - V: Payment_plan values     
        return debts_dict
            
        
