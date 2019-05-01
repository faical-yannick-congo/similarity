""" Similarity is a package/cmd that allows a similarity check between
a new record and a list of records in a store. Criteria are provided to
define the notion similarity which can be values ranges and specific
string key-value pairs contents.
"""

from setuptools import setup, find_packages
import os
import subprocess

def fetch_requirements():
    required = []
    with open('requirements.txt') as f:
        required = f.read().splitlines()
    return required

PACKAGE_NAME = "simy"


setup(name=PACKAGE_NAME,
      version='0.1',
      description='Similarity checker between a record and an existing store.',
      author='Daniel Wheeler, Lucas Hale, Faical Yannick Congo',
      author_email='yannick.congo@gmail.com',
      include_package_data=True,
      install_requires=fetch_requirements(),
      url='https://github.com/faical-yannick-congo/similarity',
      classifiers=[
        "Development Status :: 1 - Alpha",
        "Programming Language :: Python",
      ],
      packages=find_packages(),
      entry_points={
        'console_scripts': [
            'simy = simy.main.cli:handle',
        ],
      },
      test_suite='nose.collector',
      tests_require=['nose'])
