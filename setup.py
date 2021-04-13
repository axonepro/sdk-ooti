# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import sdk_ooti

setup(
    name='sdk_ooti',

    version=sdk_ooti.__version__,

    packages=find_packages(),

    author="Axonepro",

    author_email="accounts@ooti.co",

    description="SDK for ooti",

    long_description=open('README.md').read(),

    include_package_data=True,

    url='https://github.com/axonepro/sdk-ooti',

    # https://pypi.python.org/pypi?%3Aaction=list_classifiers.
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 1 - Development",
        "Natural Language :: French",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
)
