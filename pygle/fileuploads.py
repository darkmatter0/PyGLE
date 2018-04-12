# -*- coding: iso-8859-1 -*-
# Copyright (c) 2017 Jamie Bull - oCo Carbon Ltd
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""
Network observation file upload and status

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pygle.http import get
from pygle.http import post


def kml(transid):
    """Download a KML summary of a file
    
    Get a KML summary approximation for a successfully processed file uploaded
    by the current user.
    
    Parameters
    ----------
    transid : str
        The unique transaction ID for the file.
    
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return get('file', 'kml/{transid}'.format(**locals()))


def transactions(pagestart=None, pageend=None):
    """Get the status of files uploaded by the current user
    
    Paginated at 50 results per page.
    
    Parameters
    ----------
    pagestart : int, optional
        Most recent record to fetch descending chronologically. Defaults to 0.
    pageend : int, optional
        Number of results to fetch from offset. Defaults to 100.
    
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
        
    """
    return get('file', 'transactions', **locals())


def upload(file, donate=None):
    """Upload a file
    
    Transmit a file for processing and incorporation into the database.
    
    Parameters
    ----------
    file : file or file-like object
        Supports DStumbler, G-Mon, inSSIDer, Kismac, Kismet, MacStumbler, 
        NetStumbler, Pocket Warrior, Wardrive-Android, WiFiFoFum, WiFi-Where, 
        WiGLE WiFi Wardriving, and Apple consolidated DB formats. One or more 
        files may be enclosed within a zip, tar, or tar.gz archive. Files may 
        not exceed 140MiB, and archives WILL IGNORE more than 200 member files.    
    donate : boolean, optional
        Allow commercial use of the file contents - True to allow.
    
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return post('network', 'upload', **locals())
