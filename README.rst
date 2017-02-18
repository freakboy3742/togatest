Toga Test
=========

A test project to demonstrate toga in a web context.

Quickstart
----------

Get the togatest code::

    $ git clone https://github.com/freakboy3742/togatest

Create a virtual environment::

    $ cd togatest
    $ virtualenv --python=`which python3` venv
    $ . venv/bin/activate

Get the Toga code, and install it into the virtual environment::

    $ cd ..
    $ git clone https://github.com/pybee/toga
    $ cd toga/src/core
    $ pip install -e .
    $ cd ../django
    $ pip install -e .

Install the Python and Javascript requirements of togatest::

    $ cd ../../togatest
    $ pip install -r requirements.txt
    $ npm install

Compile the Javascript bundle::

    $ npm run build

Configure the togatest settings::

    $ cd togatest/settings/
    $ cp template.env .env

Open ``.env`` in your editor, and modify the contents (in particular,
the database path) to suit local conditions.

Once this is done, you can perform the initial database migration::

    $ cd ../..
    $ ./manage.py migrate

Run the Django server::

    $ ./manage.py runserver

... and reload the page. This will load the page with bootstrap styling.
If you press the "Go" button, it should load the nominated URL into the
iframe on the page.

