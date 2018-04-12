# -*- coding: iso-8859-1 -*-
# Copyright (c) 2017 Jamie Bull - oCo Carbon Ltd
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""
Statistics and information

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pygle.http import get


def apiToken(token_type=None):
    """Get all authorization tokens for the logged-in user
    
    Parameters
    ----------
    token_type : str
        Token types - 'API', 'COMMAPI', or 'ANDROID'.
        
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    params = {'type': token_type}  # required because "type" is a reserved word
    return get('profile', 'apiToken', **params)


def user():
    """Get the user object for the current logged-in user
    
    See basic user information.
    
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return get('profile', 'user')
