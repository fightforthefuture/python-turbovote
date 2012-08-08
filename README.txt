================
python-turbovote
================

python-turbovote is a lightweight Python wrapper around the TurboVote API. For 
more information on arguments or on return types, please see the TurboVote API 
documentation at http://goo.gl/Ugn9M.

Sample usage::

    from turbovote import API

    a = API(MY_TURBOVOTE_API_KEY)
    a.elections("MA")

