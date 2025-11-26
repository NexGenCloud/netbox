from os import environ

CACHE_TIMEOUT = environ.get('CACHE_TIMEOUT', 0)
