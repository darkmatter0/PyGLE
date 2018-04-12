# Copyright (c) 2017 Jamie Bull - oCo Carbon Ltd
# =======================================================================
#  Distributed under the MIT License.
#  (See accompanying file LICENSE or copy at
#  http://opensource.org/licenses/MIT)
# =======================================================================
"""
Sniff local WiFi networks in order to look them up on WiGLE.

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from platform import system
import re
import subprocess
import time

import requests

from pygle import network


scan_cmd = {'windows': 'netsh wlan show networks mode=Bssid', 
            'linux': 'nmcli -t -f bssid dev wifi list', 
            'osx': '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s',
            }
geolocate_cmd = {
    'google': 'https://maps.googleapis.com/maps/api/browserlocation/json?browser=firefox&wifi=mac:{bssid}'}


def local_bssids():
    res = subprocess.check_output(scan_cmd[system().lower()],
                                  universal_newlines=True)
    pattern = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    bssids = pattern.findall(res)
    return set(bssids)


def geolocate(geocoder):
    lats = []
    longs = []
    for bssid in local_bssids():
        print("BSSID:", bssid)
        if geocoder == 'wigle':
            lat, lng = geolocate_wigle(bssid)
        elif geocoder == 'google':
            lat, lng = geolocate_google(bssid)
        print(lat, lng)
        if lat:
            lats.append(lat)
        if lng:
            longs.append(lng)
        time.sleep(0.1)
    if lats:
        lat = sum(lats) / len(lats)
        lng = sum(longs) / len(longs)
        return lat, lng
    else:
        return "No geolocation possible"


def geolocate_wigle(bssid):
    res = network.search(netid=bssid)
    if res['success'] and res['resultCount']:
        lat = res['results'][0]['trilat']
        lng = res['results'][0]['trilong']
    else:
        print(res)
        lat, lng = None, None
    return lat, lng

        
def geolocate_google(bssid):
    res = requests.get(geolocate_cmd['google'], params={'mac': bssid})
    res.raise_for_status()
    res = res.json()
    if res['status'] == 'OK':
        lat = res['location']['lat']
        lng = res['location']['lng']
    else:
        lat, lng = None, None
    return lat, lng


if __name__ == "__main__":
    print("WiGLE")
    print(geolocate('wigle'))
    print("Google")
    print(geolocate('google'))
    