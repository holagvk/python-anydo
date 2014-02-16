#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Internet",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

setup(name="python-anydo",
      version="0.1.0",
      description="Unoffical Any.Do API client",
      license="MIT",
      install_requires=["requests"],
      author="Gaurav Kalra",
      author_email="gvkalra@gmail.com",
      url="https://github.com/gvkalra/python-anydo",
      classifiers=classifiers,
      packages=find_packages(),
      keywords="anydo",
      test_suite='anydo.tests',
      tests_require=['pep8', 'mock'],
      zip_safe=True)
