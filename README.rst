
=============
OpenResources
=============

OpenResources is a flexible, tag-based database application for Django. It has been developed for `Vivir Bien`_, a mapping platform for solidarity economy resources.

OpenResources comes with "batteries included", which means that you non't only get a Django app but also a set of templates and media files that should give you a starting point and are designed with easy customization in mind.


Dependencies
------------

All dependencies on other (non-standard) Django applications are optional. At the moment OpenResources is prepared to work with the following 3rd party Djago applications:

* Transmeta_ for multilingual installations
* django-threadedcomments_ for comments inside resources and views


Running OpenResources
---------------------

The enclosed test project allows you to run OpenResources in a local test setup without further installation. Simply run::

  manage.py syncdb

(only the first time, creates database and superuser), then::

  manage.py runserver

to run a pre-configured server. Point your browser to http://localhost:8000/ - et voilà!


Installing OpenResources
------------------------

Adding OpenResources to a Django setup should be pretty straightforward. The only setting that is required is currently::

  AUTH_PROFILE_MODULE = 'openresources.UserProfile'

(We are working on removing this need).

The included templates are expecting the OpenResources media files to be served at {{MEDIA_URL}}openresources/ , so if you want to use (or customize) these you should copy or symlink them accordingly.



.. _`Vivir Bien`: http://vivirbien.mediavirus.org/
.. _Transmeta: http://code.google.com/p/django-transmeta/
.. _django-threadedcomments: https://github.com/ericflo/django-threadedcomments
