# -*- coding: utf-8 -*-
import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from PlaystationNetworkAPI_client import *
from ZSI.twisted.wsgi import SOAPApplication, soapmethod, SOAPHandlerChainFactory, WSGIApplication

import logging

logger = logging.getLogger(__name__)


from service.services import *
 
class PlaystationNetworkAPIService(SOAPApplication):
 
    _wsdl = "".join(open("PlaystationNetworkAPI.wsdl").readlines())
    _noget = "".join(open("noget.html").readlines())
 
    @soapmethod(GetProfileSoapIn.typecode, GetProfileSoapOut.typecode, operation='GetProfile', soapaction='GetProfile' )
    def soap_GetProfile(self, request, response, **kw):
        
        logger.info("Creating CrawlerService & GetProfile")
        
        result = CrawlerService().GetProfile(request._psnId)
        # Usado para propóstios de testes apenas ;P
        #result = DummyService().GetProfile(request._psnId)
        
        logger.info("Returning Response")
        
        response.GetProfileResult = result
        
        return request, response 
    
    def _handle_GET(self, env, start_response):
        if env['QUERY_STRING'].lower() == 'wsdl':
            start_response("200 OK", [('Content-Type','text/xml')])
            return [ self._wsdl ]

        start_response("404 ERROR", [('Content-Type','text/html')])
        return [ self._noget ]
"""
    Serviço Principal que deste WS
"""    
application = WSGIApplication()
application['PlaystationNetworkAPI'] = PlaystationNetworkAPIService()
