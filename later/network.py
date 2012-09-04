#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
import cookielib
import json
import logging
import os
from random import random
import sys
import urllib
import urllib2
import urlparse

## Default set of headers for requests to PSN
DEFAULT_HEADERS = {
    'User-agent':       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)',
    'Accept':           '*/*',
    'Accept-Encoding':  'gzip, deflate',
    'Accept-Language':  'en-US',
    'Connection':       'Keep-Alive',
}

class Friend(object):

    def __init__(self, handle, opener):
        self.handle = handle
        self._online = None
        self._avatar = None
        self._playing = None
        self._opener = opener

    @property
    def online(self):
        if self._online is None:
            self._update()
        return self._online

    @property
    def avatar(self):
        if self._avatar is None:
            self._update()
        return self._avatar

    @property
    def playing(self):
        if self._playing is None:
            self._update()
        return self._playing


    def _update(self):
        url = 'http://us.playstation.com/playstation/psn/profile/%s?id=%f' % (self.handle, random())
        headers = DEFAULT_HEADERS
        headers.update({
            'Referer': 'http://us.playstation.com/playstation/psn/profile/friends?id=%f' % random(),
            'X-Requested-With': 'XMLHttpRequest',
        })
        rq = urllib2.Request(url=url, headers=headers)
        rs = unicode(self._opener.open(rq, timeout=10000).read(), errors='ignore')
        soup = BeautifulSoup(rs)

        try:
            self._avatar = soup.find('div', {'class': 'avatar'}).find('img')['src'].split('=', 1)[1]
        except:
            self._avatar = u''

        try:
            self._online = bool(soup.find('div', {'class': 'oStatus'}).find('div', {'class': 'onlineStatus online'}))
        except:
            self._online = False

        try:
            self._playing = soup.find('span', {'class': '_iamplaying_'}).text
        except:
            self._playing = u''



class PSN(object):

    def __init__(self, email, passwd, proxy=None):
        self._handle = None
        self._email = email
        self._passwd = passwd
        self._friends = None

        # Install global opener for urllib2 using a cookie fiel named after
        self._cookie_file = email.lower().strip() + '.lwp'
        self._cookie_jar = cookielib.LWPCookieJar()


        hh = urllib2.HTTPHandler()
        hsh = urllib2.HTTPSHandler()
        hh.set_http_debuglevel(1)
        hsh.set_http_debuglevel(1)
        opener = urllib2.build_opener(hh, hsh)
        logger = logging.getLogger()
        logger.addHandler(logging.StreamHandler(sys.stdout))
        logger.setLevel(logging.NOTSET)

        if proxy:
            proxy_host, proxy_port = proxy.split(':')
            self._opener = urllib2.build_opener(hh, hsh,
                urllib2.HTTPCookieProcessor(self._cookie_jar),
                urllib2.ProxyHandler({'http':'http://%s:%s' % (proxy_host,proxy_port)}))
        else:
            self._opener = urllib2.build_opener(hh, hsh, urllib2.HTTPCookieProcessor(self._cookie_jar))

    @property
    def handle(self):
        if not self._handle:
            self._login()
        return self._handle

    def _login(self):

        ## Post the login form to get a session id
        url = 'https://store.playstation.com/j_acegi_external_security_check?target=/external/login.action'
        data = {'j_username': self._email,
                'j_password': self._passwd,
                'returnURL': 'http://www.psnapi.com.ar/ps3/login.aspx'}
        headers = DEFAULT_HEADERS
        headers.update({'Referer': 'https://store.playstation.com/external/index.vm?returnURL=http://www.psnapi.com.ar/ps3/login.aspx'})
        rq = urllib2.Request(url=url, data=urllib.urlencode(data), headers=headers)

        # Store session id
        sess_id = self._opener.open(rq, timeout=10000).read()

        ## Hammer at a few urls for the proper cookies
        del headers['Referer']
        url = 'http://us.playstation.com/uwps/PSNTicketRetrievalGenericServlet?sessionId=%s' % (sess_id)
        rq = urllib2.Request(url=url, headers=headers)
        try:
            self._opener.open(rq, timeout=10000)
        except urllib2.HTTPError:
            pass # this just happens, but it needs to happen

        url = 'http://us.playstation.com/uwps/HandleIFrameRequests?sessionId=%s' % (sess_id)
        rq = urllib2.Request(url=url, headers=headers)
        self._opener.open(rq, timeout=10000)

        url = 'http://us.playstation.com/uwps/CookieHandler'
        headers.update({'Referer': 'http://us.playstation.com/portableid/index.htm'})
        rq = urllib2.Request(url=url, headers=headers)
        rs = self._opener.open(rq, timeout=10000).read()

        # Store handle
        self._handle = rs.split(',')[0].replace('handle=','')

    @property
    def friends(self):
        if self._friends is not None:
            return self._friends

        if self._handle is None:
            self._login()

        self._friends = []

        url = 'https://us.playstation.com/playstation/psn/get_friends?id=%f' % random()
        headers = DEFAULT_HEADERS
        headers.update({'Referer': 'https://us.playstation.com/myfriends/', 'X-Requested-With': 'XMLHttpRequest'})
        rq = urllib2.Request(url=url, data=urllib.urlencode({}), headers=headers)
        rs = self._opener.open(rq, timeout=10000).read()

        url = 'https://us.playstation.com/playstation/psn/profile/get_friends_names'
        headers = DEFAULT_HEADERS
        headers.update({'Referer': 'https://us.playstation.com/myfriends/'})
        rq = urllib2.Request(url=url, headers=headers)
        rs = self._opener.open(rq, timeout=10000).read()
        friend_handles = sorted(json.loads(rs), key=unicode.lower)

        for handle in friend_handles:
            self._friends.append(Friend(handle, self._opener))
        return self._friends
