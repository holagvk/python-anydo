#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        sys.exit(errno)


classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
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
      tests_require=['tox'],
      cmdclass={'test': Tox},
      zip_safe=True)
