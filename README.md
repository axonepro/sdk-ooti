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
   my_account = sdk_ooti.Auth('email', 'password')
   my_account.connect()
   ```
3. Do a request
   ```py
   invoices = my_account.get_invoices_list()
   ``` 

See the [example.py](https://github.com/axonepro/sdk-ooti/blob/master/example.py) file for more examples


<!-- LICENSE -->
## License

Copyright (C) 2016-2021 AxonePro S.A.S. legal@ooti.co All Rights Reserved

This file is part of axonepro.com.

Unauthorized copying of any file in this project, via any medium is strictly prohibited. Proprietary and confidential

axonepro.com can not be copied and/or distributed without the express permission of AXONEPRO.
