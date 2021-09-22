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
        <a href="#developer">Developer</a>
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

First, run the following command to setup your envrionment.
it will generate an ```.env``` files and install a virtuel environment

```
  make init
```

>  **note: If your are on linux, or mac Os, maybe make command line isn't installed. You should open your terminal and run**
>  - On Mac:
>  ````
    sudo xcode-select --install
>  ````
>  - On Linux:
>  ```
>  sudo apt install make
  **or**
>  sudo apt install build-essential
>  ```
> ** if you need use python3 instead python, use the command make python_alias **

Then, should edit your ```.env``` file with your username and your password

```
  ENVIRONMENT=STAGING
  OOTI_AUTH=youremail
  OOTI_PASSWORD=yourpassword
```

### Start the environment
Now, you are ready ! You could run the following command to start the virtuel environment
```
  make start
```
and to quit the virtuel envrionment you could use:
```
  make stop #TODO
```

### Run the tests

Run all tests:
```
  make tests
```

Run a specific test
```
  make test filename=my_file
```

Run a specific class test
```
  make test filename=my_file class=my_class
```

Run a specific method in test file
```
  make test filename=my_file method=my_method
```


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

### Initialize environment


<!-- LICENSE -->
## License

Copyright (C) 2016-2021 AxonePro S.A.S. legal@ooti.co All Rights Reserved

This file is part of axonepro.com.

Unauthorized copying of any file in this project, via any medium is strictly prohibited. Proprietary and confidential

axonepro.com can not be copied and/or distributed without the express permission of AXONEPRO.

# HOW TO PUBLISHED IN PYPI
French tuto: https://sametmax.com/creer-un-setup-py-et-mettre-sa-bibliotheque-python-en-ligne-sur-pypi/

Twine documentation: https://twine.readthedocs.io/en/latest/

update ooti package version
```sh
   python setup.py sdist bdist_wheel
   python3 -m twine check dist/*
   python3 -m twine upload -r pypi dist/*
   python3 twine upload dist/* --skip-existing
```

<!-- MARKDOWN LINKS & IMAGES -->
[linkedin-url]: https://www.linkedin.com/company/ooti-co/
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[contributors-url]: https://github.com/axonepro/sdk-ooti/graphs/contributors
[contributors-shield]: https://img.shields.io/github/contributors/immo/Best-README-Template.svg?style=for-the-badge
