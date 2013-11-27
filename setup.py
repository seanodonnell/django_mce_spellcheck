import os
import sys

from setuptools import setup, find_packages

version = '0.1'

setup(name='django_mce_spellcheck',
    version=version,
    packages=find_packages(exclude=['ez_setup']),
    description='',
    long_description='',
    include_package_data=True,
    zip_safe=False,
)
