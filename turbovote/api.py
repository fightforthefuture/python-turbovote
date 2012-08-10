import requests
import re

_URL_PREFIX = "https://staging.turbovote.org/api/"

def _bracketize(key):
    if "_" in key:
        m = re.match(r"^([^_]+)_(.+)$", key)
        return "{0}[{1}]".format(m.group(1), m.group(2))
    else:
        return key

def _locals(locals_dict):
    new_locals = locals_dict.copy()
    del new_locals["self"]
    return new_locals

class API(object):
    def __init__(self, api_key):
        self._api_key = api_key

    def _call(self, method, **kwargs):
        url = _URL_PREFIX + method
        params = { "token": self._api_key }
        for k, v in kwargs.items():
            params[_bracketize(k)] = v
        r = requests.get(url, params=params)
        return r.json

    def version(self):
        return self._call("version")

    def questions(self, street, city, state):
        return self._call("questions", **_locals(locals()))

    def elections(self, state=None):
        path_suffix = "/{0}".format(state) if state else ""
        return self._call("elections{0}".format(path_suffix))

    def registered(self, voter_first, voter_last, voter_state, voter_zip):
        return self._call("registered", **_locals(locals()))

    def partners(self):
        return self._call("partners")

    def create(self, voter_first, voter_last, voter_prefix, voter_suffix, 
               voter_email, voter_street, voter_city, voter_state, voter_zip, 
               voter_dob, voter_party, voter_citizen, voter_service_type, 
               voter_hostname):
        params = _locals(locals())
        params["voter_dob"] = voter_dob.strftime("%Y-%m-%d")
        params["voter_citizen"] = "true" if voter_citizen else "false"
        return self._call("create", **params)
