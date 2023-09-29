#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to that URL
And displays the value of X-Request-Id found in the header
of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
