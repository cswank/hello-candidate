Evaluating a Candidiate's Python Skill With the Hello App
=========================================================
This is a simple flask app that serves up a few resources via http GET
requests.  It has a simple bug (user objects that are returned have the age
and name swapped) and can be used to see how a person would find the bug.

I'd like to see the candidate:

1.  create a virtualenv for this package
2.  activate the virtualenv
3.  git clone the project
4.  install the project using 'python setup.py develop'
5.  run the tests using nosetests

The tests show the correct output of that the app should produce and
the messed up output that it currently produces.
