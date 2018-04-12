# -*- coding: iso-8859-1 -*-
# Copyright (c) 2017 Jamie Bull - oCo Carbon Ltd
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""
Configuration for the Wigle API.

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os


url = "https://api.wigle.net/api/v2/{section}/{endpoint}"
# Visit https://wigle.net/account to collect your API token
user = ""
key = ""

try:
    # for use in dev environment
    from pygle.dev.config import *
    print(user)
    print(key)
except ImportError:
    pass

if user == "" or key == "":
    print("Visit https://wigle.net/account to collect your API token")
    here = os.path.abspath(__file__)
    here.replace('.pyc', '.py')
    print("Then add your credentials to %s" % here)
