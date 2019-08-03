from .base import *

DEBUG = False
ALLOWED_HOSTS += ['https://api-grata.herokuapp.com/']
WSGI_APPLICATION = 'wsgi.prod.application'