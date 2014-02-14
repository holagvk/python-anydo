python-anydo
============

Unofficial python bindings for Any.Do


Preparing commit before sending pull request
--------------------------------------------

You should add bin/runtest.sh as pre-commit git-hook.
It will help you in verifying your changes locally.

	$ git clone https://github.com/gvkalra/python-anydo.git
	$ cd python-anydo
	$ cp bin/runtest.sh .git/hooks/pre-commit
