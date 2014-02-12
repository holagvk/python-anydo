#!/usr/bin/env sh

cd $(git rev-parse --show-toplevel)

#python
find . -name "*.pyc" -delete

#linux
find . -name "*~" -delete
