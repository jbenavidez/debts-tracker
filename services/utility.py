from typing import Any
from validator.debt_schema import DebtValidator
from validator.payment_plan_schema import PaymentPlanValidator
from validator.payment_schema import PaymentValidator
import logging
import sys


class UtilityService:

    @staticmethod
    def debts_validator(data:dict)-> dict:
        # this is use to validate debts dicts 
        if isinstance(data, dict):
            record = DebtValidator(**data)
        else:
            record = DebtValidator(**data.dict())
        return data

    @staticmethod
    def payment_plan_validator(data:dict)-> dict:
        # this is use to payment plans  dicts 
        if isinstance(data, dict):
            record = PaymentPlanValidator(**data)
        else:
            record = PaymentPlanValidator(**data.dict())
        return data

    @staticmethod
    def payment_validator(data:dict)-> dict:
        # this is use to  plans  dicts 
        if isinstance(data, dict):
            record = PaymentValidator(**data)
        else:
            record = PaymentValidator(**data.dict())
        return data       

    @staticmethod
    def get_logger(name) -> Any:
        # this is used to create a logger
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_handler.setFormatter(formatter)
        file_handler = logging.FileHandler('storage/logs/app.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stdout_handler)
        return logger