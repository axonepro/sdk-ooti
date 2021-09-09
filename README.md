<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/axonepro/sdk-ooti/blob/master/README.md">
    <img src="ooti/logo.png" alt="Logo" width="240" height="140">
  </a>

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
   import sdk_ooti
   ```
2. Connect to the API
   ```py
   my_account = sdk_ooti.OotiAPI('email', 'password')
   my_account.connect()
   ```
3. Do a request
   ```py
   invoices = my_account.get_invoices_list()
   ``` 

## Example

```
import ooti
import pprint


###### Connect ######
my_account = ooti.OotiAPI('email', 'password')
my_account.connect()


###### Invoice ######
invoices = my_account.get_invoices_list()  # Get the list of invoices
for invoice in invoices:
    pprint.pp(invoice)  # Print each invoice

invoice = my_account.get_invoice_details(pk='invoice_pk')  # Get the details of one invoice
for line in invoice['items']:
    pprint.pp(line)  # Print each lines of the invoice

payload = {
    "amount": 1000,
}
invoice = my_account.create_invoice(1499, payload)  # Create an invoice
pprint.pp(invoice)

payload = {
    "amount": 3000,
}
invoice = my_account.update_invoice(pk='invoice_pk', payload)  # updatee an invoice
pprint.pp(invoice)

###### Payment ######
payments = my_account.get_payments_list()  # Get the list of payments
for payment in payments:
    pprint.pp(payment)  # Print each payment

payment = my_account.get_payment_details(pk='payment_pk')  # Get the details of one payment
pprint.pp(payment)

payload = {
    "amount": 1000,
}
payment = my_account.create_payment(1499, payload)  # Create an payment
pprint.pp(payment)

payload = {
    "amount": 3000,
}
payment = my_account.update_payment(pk='payment_pk', payload)  # updatee an payment
pprint.pp(payment)

###### Project ######
projects = my_account.get_projects_list()  # Get the list of projects
for project in projects:
    pprint.pp(project)  # Print each project

project = my_account.get_project_details(pk='invoice_pk')  # Get the details of one project
pprint.pp(project)  # Print details of the project

data = {
    'business_title': 'new_title'
}
project = my_account.update_project_details(pk='invoice_pk', data=data)  # Update the details of one project
pprint.pp(project)  # Print details of the updated project


###### Phase ######
phases = my_account.get_phases_list(project_pk='invoice_pk')  # Get the list of phases
for phase in phases:
    pprint.pp(phase)  # Print each phase

phase = my_account.get_phase_details(pk='phase_pk')  # Get the details of one phase
pprint.pp(phase)  # Print details of the phase

data = {'progress': 66}
phase = my_account.update_phase_details(pk='phase_pk', data=data)  # Update the details of one phase
pprint.pp(phase)  # Print details of the updated phase
```

<!-- LICENSE -->
## License

Copyright (C) 2016-2021 AxonePro S.A.S. legal@ooti.co All Rights Reserved

This file is part of axonepro.com.

Unauthorized copying of any file in this project, via any medium is strictly prohibited. Proprietary and confidential

axonepro.com can not be copied and/or distributed without the express permission of AXONEPRO.
