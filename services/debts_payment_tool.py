from .debts_service import DebtsService
from .payment_plan_service import PaymentPlanService
from .payment_service import PaymentService
from .utility import UtilityService
from typing import Dict, List
import traceback
from datetime import datetime

class DebtsPaymentsTool:
    """
    this services is an internal admin tool which is used to handle payment process task
    """
    debts = DebtsService.get_debts()
    payment_plans = PaymentPlanService.get_payment_plans()
    payments = PaymentService.get_payments()
    logger = UtilityService.get_logger(__name__)
    payment_frecuency = {
                    "WEEKLY": 7, # after 7 days payment should be done
                    "BI_WEEKLY": 14, # after 15 days payment should be done

                    }

    @classmethod
    def get_payments(cls, payment_plan: Dict) -> Dict:
        # this func is used to get all the payment by plan_id
        payment_plan_id = payment_plan['id']
        # Get payment records
        payments_records = cls.payments[payment_plan_id]
        cls.logger.info(f"Getting payments info for payment_plan_id: {payment_plan_id}")
        return payments_records

    @classmethod
    def check_if_payment_on_time(cls, payments: List[Dict], installment_frequency: str) -> bool:
        # this func checks is all payment are on time
        cls.logger.info(f"checking if payments are on time")
        is_payment_on_time = True
        start_payment =  datetime.strptime(payments[0]['date'], "%Y-%m-%d")
        for idx, item in enumerate(payments[1:]):
            tempt_date = datetime.strptime(item['date'], "%Y-%m-%d")
            diff = tempt_date - start_payment
            if diff.days != cls.payment_frecuency[installment_frequency]:
                return False # payment are not being pay on time
            start_payment = tempt_date
        return is_payment_on_time

    @classmethod
    def cal_remaing_debt_amount(cls, debts: float, payment_plan: Dict, payments:Dict) -> float:
        # this func is used to cal remaining amount 
        total_amount = debts
        amount_to_pay = payment_plan['amount_to_pay']
        total_payment= sum([x['amount'] for x in payments]) # cal total payment
        remaining_amount  = amount_to_pay - total_payment
        cls.logger.info(f"calculating remaining amount for payment_plan_id: {payment_plan['id']}")
        return remaining_amount

    @classmethod
    def get_debts_info(cls) -> List[Dict]:
        # this is used to process the task on the assimgne
        debts_list = []
        debts_objs = cls.debts
        for debt_k, v in debts_objs.items():
            # Get payment plans 
            payment_plan = cls.payment_plans.get(debt_k)
            cls.logger.info(f"setting debts is_in_payment_plan flag for debt_id: {debt_k}")
            if payment_plan is not None:
                # if payment_plan exist get payments info
                payments = cls.get_payments(payment_plan)
                # set is_in_payment_plan 
                debts_objs[debt_k]['is_in_payment_plan'] = True 
                # add remainng_amounts
                remaining_amount = cls.cal_remaing_debt_amount(v['amount'],payment_plan,payments)
                debts_objs[debt_k]['remaining_amount']  = remaining_amount
                # check if payment are on time 
                is_payment_on_time = cls.check_if_payment_on_time(payments, payment_plan['installment_frequency'])
                debts_objs[debt_k]['is_payment_on_time'] = is_payment_on_time

            else:
                # debt lacking payment plan
                debts_objs[debt_k]['is_in_payment_plan'] = False 
            debts_list.append(v)
        print(debts_list)
        return debts_list
        
 