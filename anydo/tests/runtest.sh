#!/usr/bin/env sh

clean () {
	#python
	find . -name "*.pyc" -delete

	#linux
	find . -name "*~" -delete
}

cd $(git rev-parse --show-toplevel)
clean

python setup.py test
python setup.py check -r || exit 1
if which pychecker > /dev/null; then
	pychecker -X -s anydo/*.py
	pychecker -X -s anydo_tests/*py
fi
clean
