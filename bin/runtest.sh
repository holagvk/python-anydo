#!/usr/bin/env sh

clean () {
	#python
	find . -name "*.pyc" -delete

	#linux
	find . -name "*~" -delete
}

cd $(git rev-parse --show-toplevel)
clean

if which pip > /dev/null; then
    pip install --upgrade pylint
    pip install --upgrade tox
    pylint --rcfile=.pylint.rc anydo/*.py anydo/lib/*.py anydo/lib/tests/*.py
    tox
fi

clean
