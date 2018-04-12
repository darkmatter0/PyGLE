# -*- coding: iso-8859-1 -*-
# Copyright (c) 2017 Jamie Bull - oCo Carbon Ltd
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""
Network search and information tools 

"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from pygle.http import get
from pygle.http import post


def comment(netid, comment):
    """Add a comment to a network
    
    Provide custom information regarding a single network.
    
    Parameters
    ----------
    netid : str
        The BSSID of the network for the comment, e.g. '0A:2C:EF:3D:25:1B'.
    comment : str    
        The comment to attach.
        
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return post('network', 'comment', **locals())
    
    
def detail(netid=None, operator=None, lac=None, cid=None, system=None,
           network=None, basestation=None):
    """Get details and observation records for a single network
    
    Provide unique information for a WiFi or cell network to request detailed 
    information. Providing a netId value searches WiFi, operator searches GSM, 
    and system searches CDMA.
    
    Parameters
    ----------
    netid : str, optional
        The WiFi Network BSSID to search.
    operator : int, optional
        GSM Operator ID.
    lac : int, optional
        GSM Location Area Code.
    cid : long, optional
        GSM Cell ID.
    system : int, optional
        CDMA System ID.
    network : int, optional
        CDMA Network ID.
    basestation : int, optional
        CDMA Base Station ID.
    
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return get('network', 'detail', **locals())
    

def geocode(addresscode=None):
    """Get coordinates for an address for use in searching
    
    Relies on OpenStreetMap nominatim.
    
    Parameters
    ----------
    addresscode : str
        An address string, Street, City, State/Region, Country.
    
    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return get('network', 'geocode', **locals())
    
    
def search(onlymine=None, first=None, latrange1=None, latrange2=None,
           longrange1=None, longrange2=None,
           lastupdt=None, freenet=None, paynet=None, netid=None, 
           ssid=None, ssidlike=None, variance=None, resultsPerPage=None):
    """Search the WiGLE database
    
    Query the WiGLE database for paginated results based on multiple criteria. 
    API and session authentication default to a page size of 100 results/page. 
    COMMAPI defaults to a page size of 25 with a maximum of 1000 results per 
    return. Number of daily queries allowed per user are throttled based on 
    history and participation
    
    Parameters
    ----------
    onlymine : boolean, optional
        Search only for points first discovered by the current user. Use any 
        string to set, leave unset for general search. Can't be used with 
        COMMAPI auth, since these are points you have locally.
    first : int, optional
        Result offset to fetch, used to page through results. Defaults to 0. 
        COMMAPI queries are bounded at 100 pages. If you need more open-ended 
        searches than this, we recommend contacting WiGLE-admin@wigle.net to 
        discuss bulk pricing.
    latrange1 : float, optional
        Lesser of two latitudes by which to bound the search.
    latrange2 : float, optional
        Greater of two latitudes by which to bound the search.
    longrange1 : float, optional
        Lesser of two latitudes by which to bound the search.
    longrange2 : float, optional
        Greater of two longitudes by which to bound the search.
    lastupdt : str, optional
        Filter points by how recently they've been updated, condensed date/time
        numeric string format 'yyyyMMddhhmmss'
    freenet : boolean, optional
        Include only networks that have been marked as free access.
    paynet : boolean, optional
        Include only networks that have been marked as for-pay access.
    netid : str, optional
        Include only networks matching the string network BSSID, e.g. 
        '0A:2C:EF:3D:25:1B' or '0A:2C:EF'. The first three octets are required.
    ssid : str, optional
        Include only networks exactly matching the string network name.
    ssidlike : str, optional
        Include only networks matching the string network name, allowing
        wildcards '%' (any string) and '_' (any character).
    variance : float, optional
        How tightly to bound queries against the provided latitude/longitude
        box. Value must be between 0.001 and 0.2
    resultsPerPage : int, optional
        How many results to return per request. Defaults to 25 for COMMAPI, 10
        for site. Bounded at 1000 for COMMAPI, 100 for site.

    Returns
    -------
    dict
    
    Raises
    ------
    requests.HTTPError
    
    """
    return get('network', 'search', **locals())
