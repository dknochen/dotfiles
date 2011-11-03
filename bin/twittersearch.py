#!/usr/bin/env python
# coding=utf-8
"""
twittersearch.py
2011, Mike Tigas
https://mike.tig.as/

Open up the Twitter streaming API and follow a search on your screen.

Usage:
    twittersearch.py
        Prompts for username and password (using getpass() so it doesn't echo
        your input) unless the TWITTER_USERNAME and TWITTER_PASSWORD
        environment variables are set.

        Prompts for search term.

    twittersearch.py [search terms]
        As above, but does not prompt for search term.


Examples:
    twittersearch.py
    twittersearch.py rick perry
    twittersearch.py bieber
"""
from urllib import urlencode
import urllib2
import json
import os
import sys
from getpass import getpass


def main(username, password, search_term):
    # We need HTTP basic auth and SSL, so build a urlopener for this
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "https://stream.twitter.com/"
    password_mgr.add_password(None, top_level_url, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    ssl = urllib2.HTTPSHandler()
    opener = urllib2.build_opener(handler, ssl)

    # Search arguments.
    # Look at https://dev.twitter.com/docs/streaming-api/methods#track
    querystring = urlencode({'track': search_term})

    # Open the stream.
    f = opener.open(
        "https://stream.twitter.com/1/statuses/filter.json?" + querystring
    )

    print "https://stream.twitter.com/1/statuses/filter.json?" + querystring
    print

    # Buffered read through the stream (possible since file objects are
    # iterable by line). The stream also blocks until more data comes in,
    # so it's cool to do this.
    for line in f:
        data = json.loads("[%s]" % line)
        if not data:
            continue

        tweet = data[0]

        # http://dev.twitter.com/doc/get/statuses/public_timeline
        # for example tweet payload
        if 'user' in tweet and 'text' in tweet:
            print "@%(screen_name)s (%(name)s)" % tweet['user']
            print tweet['created_at']
            print "https://twitter.com/%s/status/%s" % (
                tweet['user']['screen_name'],
                tweet['id_str']
            )
            print tweet['text']
            print

    f.close()

if __name__ == "__main__":
    username = os.environ.get("TWITTER_USERNAME", None)
    if not username:
        username = raw_input("Twitter Username:\n")
        print

    password = os.environ.get("TWITTER_PASSWORD", None)
    if not password:
        password = getpass("Twitter Password for %s:\n" % username)
        print

    if len(sys.argv) > 1:
        searchstr = " ".join(sys.argv[1:])
        print "Searching for tweets containing...\n'%s'\n" % searchstr
    else:
        searchstr = raw_input("Search tweets containing...\n")
        print

    main(username, password, searchstr)
