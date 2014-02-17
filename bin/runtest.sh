#!/usr/bin/env sh

clean () {
	#python
	find . -name "*.pyc" -delete

	#linux
	find . -name "*~" -delete
}

cd $(git rev-parse --show-toplevel)
clean

python setup.py test || exit 1
python3 setup.py test || exit 1
python setup.py check -r || exit 1
python3 setup.py check -r || exit 1
if which pychecker > /dev/null; then
	pychecker -X -s anydo/*.py || exit 1
	pychecker -X -s anydo/tests/*py || exit 1
fi
clean
