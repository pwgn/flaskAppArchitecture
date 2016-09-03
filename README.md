Inspired by:
https://github.com/mattupstate/overholt


System requirements
===================

```bash
sudo apt-get install python-dev python-pip postgresql-9.3 postgresql-server-dev-9.3
```

Setup database
==============

```bash
# Enter postgresql shell:
psql postgres

# Setup database
CREATE DATABASE app;

# Set user password
ALTER USER postgres WITH PASSWORD '123';
```

Virtual env
===========

```bash
# Enter postgresql shell:
psql postgres

# Setup database
CREATE DATABASE app;

# Set user password
ALTER USER postgres WITH PASSWORD '123';
```

Virtual env
===========
``` bash
sudo pip install virtualenv
virtualenv env
env/bin/pip install -r requirements.txt
```

Fronted
=======

``` bash
# Install dependencies
sh frontend/install.sh

# Complie coffescript to javascript in application
coffee --compile --output frontend/scripts/lib/ frontend/scripts/src/
```

Run
===

`env/bin/python wsgi.py`

Now the application should be available at

`http://localhost:5000`
