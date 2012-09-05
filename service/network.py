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

class BasePageParser:
    """
        Classe base para os parsers
    """
    def __init__(self, html):
        self._soup = BeautifulSoup(html)
        logger.info("Create BeautifulSoup for html %s" % (html))
    
    def _findById(self,id):
        return self._soup.find('div', id=id ).contents[0]
    
    def _findByClass(self,className):
        return self._soup.find('div', class_ = className ).contents[0]
 

class TrophiePageParser(BasePageParser):
    """
        Clase que faz o parser dos Troféus e do Perfil
    """
    def __init__(self, rs):
        self._soup = BeautifulSoup(rs)
        logger.info("Create BeautifulSoup for response %s" % (rs))

    def PsnId(self):
        return self._findById("id-handle" ).strip()
        
    def AvatarSmall(self) :
        return self._soup.find('div', id="id-avatar" ).find('img')['src'].split('=',1)[1]
        
    def Level(self) :
        return int(self._findById("leveltext" ))
        
    def Progress(self) :     
        return int(self._findByClass("progresstext").replace('%',''))

    def Platinum(self) :
        return int(self._findByClass("text platinum").replace('Platinum',''))
    
    def Gold(self) :
        return int(self._findByClass("text gold").replace('Gold',''))
    
    def Silver(self) :
        return int(self._findByClass("text silver").replace('Silver',''))
    
    def Bronze(self) :
        return int(self._findByClass("text bronze").replace('Bronze',''))
    
    def Total(self) :
        return int(self._soup.find('div', id="totaltrophies" ).find('div', id="text").contents[0])

class GamesPageParser(BasePageParser):
    """
        Classe que faz o Parser dos Jogos
    """
    
    def Title(self):
        return self._soup.find('span', class_ = 'gameTitleSortField').contents[0]
    
    def __iter__(self):
        games = []
        nodes = self._soup.find_all('div', class_ = 'slot')
        logger.info("Found %d nodes" % len(nodes)) 
        for node in nodes :
            games.append(GamesPageParser(str(node)))
        return iter(games)    

class PSN:
    """
        Classe principal de acesso ao conteúdo do site da PSN
    """

    def __init__(self, email, passwd):
        self._email = email
        self._passwd = passwd

        # Install global opener for urllib2 using a cookie fiel named after
        self._cookie_file = email.lower().strip() + '.lwp'
        self._cookie_jar = cookielib.LWPCookieJar()

        self._opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self._cookie_jar))
        
        logger.info("Finish PSN init")
        
        self._login()

    def _getUrl(self,url,referer=None,data=None):
        logger.info("GET %s" % (url))
        logger.info("Referer %s" % (referer))
        logger.info("Data %s" % (data))
        
        headers = DEFAULT_HEADERS
        if referer is not None :
            headers.update({'Referer': referer })
        
        if data is not None :
            data = urllib.urlencode(data)
        
        rq = urllib2.Request(url=url, data=data, headers=headers)
        
        try:
            rs = self._opener.open(rq, timeout=10000)
        except urllib2.HTTPError:
            logger.warning("Bypass HTTP ERROR")
            pass # this just happens, but it needs to happen

        if rs.info().get('Content-Encoding') == 'gzip':
            logger.info("Reponse is Gzipped, decompressing")
            return self._uncompress(rs)
        else :
            return rs.read()
        
    def _uncompress(self,rs):
        # Resposta está Comprimida, devo descomprimí-la
        buf = StringIO( rs.read() )
        f = gzip.GzipFile(fileobj=buf)
        return f.read()


    def _login(self):
        logger.info("Logging in")

        ## Post the login form to get a session id
        data = {'j_username': self._email,
                'j_password': self._passwd,
                'returnURL': LOGIN_RETURN }
        
        self._getUrl(LOGIN_URL,LOGIN_LANDING,data)
        
        # Store session id
        for cookie in self._cookie_jar:
            logger.info('%s --> %s'%(cookie.name,cookie.value))
            if(cookie.name == "JSESSIONID") :
                sess_id = cookie.value
        
        logger.info("Logged in with session ID=%s" % (sess_id))

        ## Hammer at a few urls for the proper cookies
        self._getUrl(TICKET_URL % (sess_id))

        logger.info("Got Ticket")

    def trophies(self,psnId):

        html = self._getUrl(PSN_PROFILE % (psnId), PING_PAGE % (psnId))

        return TrophiePageParser(html)
    
    def games(self,psnId):
        
        html = self._getUrl(PSN_GAMES % (psnId), PSN_PROFILE % (psnId))
        
        return GamesPageParser(html)