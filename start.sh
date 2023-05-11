#!/bin/sh

#
# bootstrap the virtual env if necessary
#
export FLASK_APP=__init__.py
export FLASK_DEBUG=1
export FLASK_ENV=development

flask run --host=0.0.0.0 --port=3000