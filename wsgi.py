"""WSGI runner."""

import os
import sys

sys.path.append(os.path.dirname(__file__))

from app import get_app
from settings import ProdConfig

flask_app = get_app(ProdConfig)

def application(environ, start_response):
    """WSGI application."""
    os.environ['KRB5CCNAME'] = environ['KRB5CCNAME']
    return flask_app(environ, start_response)
