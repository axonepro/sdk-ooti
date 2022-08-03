[![Build Status](https://app.travis-ci.com/axonepro/sdk-ooti.svg?branch=master)](https://app.travis-ci.com/axonepro/sdk-ooti)

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">SDK OOTI</h3>

  <p align="center">
    <a href="https://github.com/axonepro/sdk-ooti/blob/master/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://ooti.co/">ooti.co</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#how-to-use">How to use</a>
    </li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This sdk is for all people wanting to use the ooti API


### Built With

* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.7
  - https://www.python.org/downloads/release/python-377/


### Installation
In case you work with virtuel environment you could, add ooti-api in your requirements.

Run  the following command to install package ```ooti-api```:
```sh
   pip install ooti-api
```

<!-- HOW TO USE -->
## How to use

1. Import
   ```py
   import resources import ooti
   ```
2. Connect to the API
   ```py
   my_account = ooti.OotiAPI('email', 'password')
   my_account.connect()
   ```
3. Do a request
   ```py
   invoices = my_account.Invoices.get_invoices_list()
   ```

## Example

```py
from resources import ooti
import pprint


###### Connect ######
my_account = ooti.OotiAPI('email', 'password')
my_account.connect()


###### Invoice ######
invoices = my_account.Invoices.get_invoices_list()
for invoice in invoices['data']:
    pprint.pprint(invoice)

invoice = my_account.Invoices.get_invoice_details(pk='invoice_pk')
if(invoice['status']==404):
    print('check the pk as it must be false')
else:
    pprint.pprint(invoice['data'])

payload = {
    "amount": 1000,
}
invoice = my_account.Invoices.create_invoice(1499, payload)
pprint.pprint(invoice)

payload = {
    "amount": 3000,
}
invoice = my_account.Invoices.update_invoice(pk='invoice_pk', payload)
pprint.pprint(invoice)

###### Payment ######
payments = my_account.Payments.get_payments_list()
for payment in payments['data']:
    pprint.pprint(payment)

payment = my_account.Payments.get_payment_details(pk='payment_pk')
if(payment['status']==404):
    print('check the pk as it must be false')
else:
    pprint.pprint(payment['data'])

payload = {
    "amount": 1000,
}
payment = my_account.Payments.create_payment(1499, payload)
pprint.pprint(payment)

payload = {
    "amount": 3000,
}
payment = my_account.Payments.update_payment(pk='payment_pk', payload)
pprint.pprint(payment)

###### Project ######
projects = my_account.Projects.get_projects_list()
for project in projects['data']:
    pprint.pprint(project)

project = my_account.Projects.get_project_details(id='project_id')
if(project['status']==404):
    print('check the id as it must be false')
else:
    pprint.pprint(project['data'])

data = {
    'business_title': 'new_title'
}
project = my_account.Projects.update_project_details(pk='invoice_pk', data=data)
pprint.pprint(project)


###### Phase ######
phases = my_account.Phases.get_phases_list(project_pk='project_id')
for phase in phases['data']:
    pprint.pprint(phase)

phase = my_account.Phases.get_phase_details(pk='phase_id')
if(phase['status']==404):
    print('check the id as it must be false')
else:
    pprint.pprint(phase['data'])

data = {'progress': 66}
phase = my_account.Phases.update_phase_details(pk='phase_pk', data=data)
pprint.pprint(phase)
```

<!-- LICENSE -->
## License

Copyright (C) 2016-2022 AxonePro S.A.S. info@ooti.co All Rights Reserved

This file is part of ooti.co.

Unauthorized copying of any file in this project, via any medium is strictly prohibited. Proprietary and confidential

axonepro.com can not be copied and/or distributed without the express permission of AXONEPRO.
