#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name="python-anydo",
      version="0.1.0",
      description="Unoffical Any.Do API client",
      license="MIT",
      install_requires=["requests"],
      author="Gaurav Kalra",
      author_email="gvkalra@gmail.com",
      url="https://github.com/gvkalra/python-anydo",
      packages=find_packages(),
      keywords="anydo",
      test_suite='anydo_tests',
      zip_safe=True)
