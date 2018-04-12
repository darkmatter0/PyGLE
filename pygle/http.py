# -*- coding: iso-8859-1 -*-
# Copyright (c) 2017 Jamie Bull - oCo Carbon Ltd
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""
API wrapper for Wigle, WiFi geolocation.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests

from pygle.config import key
from pygle.config import url
from pygle.config import user


auth = requests.auth.HTTPBasicAuth(user, key)


def get(section, endpoint, **kwargs):    
    """Make a GET request using Basic auth.

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    path = url.format(**locals())
    r = requests.get(path, auth=auth, params=kwargs)
    r.raise_for_status()
    return r.json()
    

def post(section, endpoint, **kwargs):    
    """Make a POST request using Basic auth.

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    r = requests.post(url.format(**locals()),
                      auth=auth,
                      params=kwargs)
    r.raise_for_status()
    return r.json()
