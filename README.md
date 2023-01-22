# Python Libraries & dependencies
<ul>
<li>Pydantic</li>
<li>Virtual EN</li>
</ul>

## Description 
This project will compute customer debts, it will combines 3 differents APIS response to create a ETL process 
## Goals  
<ul>
<li>  Calculate if debts belong to an payment plan</li>
<li>Calculate is debts are being pay on time</li>
<li>Calculate debts remaining</li>
</ul>
## Instructions

### Set Enviroment 
<ol>
<li>Run  "<b>python3 -m venv env</b>" to create a virtual machine</li>
<li>Run  "<b>source env/bin/activate</b>" to activate your virtual machine</li>
<li>Run  "<b>pip3 install -r requirements.txt</b>" to install the the dependencies your virtual machine</li>
</ol>
 
 ### Execute Script 
<ul>
<li>On your terminal run  "<b>python3 app.py</b>" to run the script</li>
</ul>

## Core | Project Structure

### Services 

#### DebtsService
this services fetch and debts info from the API, and it comtain all our logic relate to debts 

#### PaymentPlanService
This services is use to get data from the payment API and all the logic relate to payment plan

#### PaymentService
This services is use to get data from the payment API and all the logic relate to payment

#### DebtsPaymentsTool
This revices is use to compute our debts objects, it calculate if payments are on time, and it calculate the reaming amounts

#### UtilityService
this services is contains logger, and common methods that we are using in our proccess

### Validators
for each data response that we get from our APIs, I created a pandactic model, to validate each item on the responses

### Storege

#### Logs
app.log file contains all the logg during our fetch/transform data


### TEST 

