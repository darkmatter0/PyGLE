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


def countries():
    """Get statistics organized by country
    
    Fetches all countries and basic stats.

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'countries')


def general():
    """Get a named map of general statistics

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'general')


def group():
    """Get group standings

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'group')


def regions(country=None):
    """Get statistics for a specified country, organized by region
    
    Parameters
    ----------
    country : str, optional
        The two-letter code of the country for which you'd like a regional 
        breakdown. Defaults to 'US'

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'regions', **locals())


def site():
    """Get a named map of site-level statistics
    
    A big hash of short-named statistics used in providing site-wide 
    information.

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'site')


def standings(sort=None, pagestart=None, pageend=None):
    """Get user standings
    
    Parameters
    ----------
    sort : str
        The criteria by which to sort the results. Values are ['discovered', 
        'total', 'monthcount', 'prevmonthcount', 'gendisc', 'gentotal', 
        'firsttransid', 'lasttransid'].
    pagestart : int
        The first record to request according to the 'sort' parameter.
    pageend : int
        The last record to request according to the 'sort' parameter.

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'standings', **locals())


def user():
    """Get user statistics

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('stats', 'user')
