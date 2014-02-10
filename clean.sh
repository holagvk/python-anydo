#!/usr/bin/env bash

#python
find . -name "*.pyc" -exec rm -rf {} \;

#linux
find . -name "*~" -exec rm -rf {} \;
