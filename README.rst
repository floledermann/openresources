About OpenResources
===================

OpenResources is a flexible, tag-based database application for Django. It has been developed for `Vivir Bien`_, a mapping platform for solidarity economy resources.

Dependencies
------------

* Transmeta_ for multilingual installations

Running OpenResources
---------------------

The enclosed test project allows you to run OpenResources in a local test setup without further installation. Simply run::

  manage.py syncdb

(only the first time, creates database and superuser), then::

  manage.py runserver

to run a pre-configured server. Point your browser to http://localhost:8000/ - et voilà!


.. _`Vivir Bien`: http://vivirbien.mediavirus.org/
.. _Transmeta: http://code.google.com/p/django-transmeta/
