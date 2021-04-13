<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/axonepro/sdk-ooti/blob/master/README.md">
    <img src="sdk_ooti/logo.png" alt="Logo" width="240" height="140">
  </a>

  <h3 align="center">SDK OOTI</h3>

  <p align="center">
    <a href="https://github.com/axonepro/sdk-ooti/blob/master/README.md"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://app.ooti.co/api/v1/docs/">Swagger: Docs API</a>
    ·
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

1. Install virtual Environment
   ```sh
   pip install pipenv
   pipenv shell --python 3.7
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
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


<!-- CONVENTIONS -->
## Conventions

### Python:
* Use docstring
* 120 character limit
* No python file greater than 2000 lines
* Follow pep8 https://www.python.org/dev/peps/pep-0008/
* In VisualStudio Code use ‘autopep8’: ("python.formatting.provider": "autopep8")


### Branch names:
* feature-xxx
* improve-xxx
* bug-xxx
* hotfix-xxx

1 commit per modification

Use informative commit messages

learn more - https://gist.github.com/digitaljhelms/4287848

### Key words:
* TODO: something todo
* TOOSLOW: Speed needs to be improved

### Imports:
Good:
   ```py
   from operations.factories import OperationFactory
   from discounts.selectors import discount_coefficient
   from discounts.selectors import discount_list
   ```
Not good:
   ```py
   from operations.factories import OperationFactory
   from discounts.selectors import (discount_coefficient,
                                    discount_list)
   ```  

<!-- LICENSE -->
## License

Copyright (C) 2016-2021 AxonePro S.A.S. legal@ooti.co All Rights Reserved

This file is part of axonepro.com.

Unauthorized copying of any file in this project, via any medium is strictly prohibited. Proprietary and confidential

axonepro.com can not be copied and/or distributed without the express permission of AXONEPRO.

# HOW PUBLISHED IN PYPI
French tuto: https://sametmax.com/creer-un-setup-py-et-mettre-sa-bibliotheque-python-en-ligne-sur-pypi/

Twine documentation: https://twine.readthedocs.io/en/latest/
```sh
   python setup.py sdist bdist_wheel
   python3 -m twine check dist/*
   python3 -m twine upload -r pypi dist/*
```

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-url]: https://www.linkedin.com/company/ooti-co/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[contributors-url]: https://github.com/axonepro/sdk-ooti/graphs/contributors
[contributors-shield]: https://img.shields.io/github/contributors/immo/Best-README-Template.svg?style=for-the-badge
