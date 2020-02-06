==============
 Contributing
==============

Issues and PRs are appreciated.

Tests
#####

Run ``python setup.py test`` to run tests against your current Python version.
Run ``tox`` to test all supported Python versions.
Configure Travis CI for your repo so that the full test suite (all combinations
of Python versions and SQLAlchemy versions supported) is run against your branch

Python Versions
###############

When the list of supported Python versions is changed, the following files need
to be updated:

* setup.py (Classifiers)
* tox.ini (tox envlist)
* .travis.yml (python section)
