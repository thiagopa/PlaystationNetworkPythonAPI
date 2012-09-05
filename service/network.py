#-*- coding: utf-8 -*-

import cookielib
import logging
import urllib
import urllib2
import urlparse
from StringIO import StringIO
import gzip

import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from bs4 import BeautifulSoup

from settings import *

logger = logging.getLogger(__name__)

class TrophiePageParser:

    def __init__(self, rs):
        self._soup = BeautifulSoup(rs)
        logger.info("Create BeautifulSoup for response %s" % (rs))

    def PsnId(self):
        return self._soup.find('div', id="id-handle" ).contents[0].strip()
        
    def AvatarSmall(self) :
        return self._soup.find('div', id="id-avatar" ).find('img')['src'].split('=',1)[1]
        
    def Level(self) :
        return int(self._soup.find('div', id="leveltext" ).contents[0])
        
    def Progress(self) :     
        return int(self._soup.find('div', {'class' : 'progresstext'} ).contents[0].split('%',1)[0])



class PSN:

    def __init__(self, email, passwd):
        self._handle = None
        self._email = email
        self._passwd = passwd
        self._friends = None

        # Install global opener for urllib2 using a cookie fiel named after
        self._cookie_file = email.lower().strip() + '.lwp'
        self._cookie_jar = cookielib.LWPCookieJar()

        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookie_jar))
        
        logger.info("Finish PSN init")
        
        self._login()

    def _login(self):
        logger.info("Logging in")

        ## Post the login form to get a session id
        url = LOGIN_URL

        data = {'j_username': self._email,
                'j_password': self._passwd,
                'returnURL': LOGIN_RETURN }
        headers = DEFAULT_HEADERS
        headers.update({'Referer': LOGIN_LANDING })
        rq = urllib2.Request(url=url, data=urllib.urlencode(data), headers=headers)

        # Store session id
        self._opener.open(rq, timeout=10000).read()
        
        for cookie in self._cookie_jar:
            logger.info('%s --> %s'%(cookie.name,cookie.value))
            if(cookie.name == "JSESSIONID") :
                sess_id = cookie.value
        
        logger.info("Logged in with session ID=%s" % (sess_id))

        ## Hammer at a few urls for the proper cookies
        del headers['Referer']
        url = TICKET_URL % (sess_id)
        rq = urllib2.Request(url=url, headers=headers)
        try:
            self._opener.open(rq, timeout=10000)
        except urllib2.HTTPError:
            pass # this just happens, but it needs to happen

        logger.info("Got Ticket")


    def trophies(self,psnId):

        logger.info("Getting Trophies")

        url = PSN_PROFILE % (psnId)
        headers = DEFAULT_HEADERS
        headers.update({'Referer': PING_PAGE % (psnId), 'X-Requested-With': 'XMLHttpRequest'})
        
        rq = urllib2.Request(url=url, headers=headers)
        
        rs = self._opener.open(rq, timeout=10000)
        
        # Resposta está Comprimida, devo descomprimí-la
        buf = StringIO( rs.read() )
        f = gzip.GzipFile(fileobj=buf)
        html = f.read()

        logger.info("Creating TrophiePageParser")

        return TrophiePageParser(html)
