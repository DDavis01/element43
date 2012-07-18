element43
=========

Market, Trade and Industry Manager for Eve Online

Setup Instructions
------------------

* Make sure you have git installed.
* Create a virtualenv.
* ``pip install -r requirements.txt``
* Create a ``element43`` user and DB on Postgres.
* ``cd webapp`` then ``python manage.py syncdb``, and ``python manage.py migrate``
* You should then be ready to run the development webserver: ``python manage.py runserver``
* Create a ``local_settings.py`` file and copy/paste/modify anything
  from ``settings.py`` that you'd like to change. This file won't be committed
  to git, and is safe to store passwords and dev workstation settings.