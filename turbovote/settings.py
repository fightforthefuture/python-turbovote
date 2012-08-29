from os import environ


def _setting(key, default):
    if key in environ:
        return environ[key]
    return default

URL_PREFIX = _setting('TURBOVOTE_URL_PREFIX', 'https://turbovote.net/api/')
