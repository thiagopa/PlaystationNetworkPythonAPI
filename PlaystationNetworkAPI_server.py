import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from PlaystationNetworkAPI_client import *
from ZSI.twisted.wsgi import SOAPApplication, soapmethod, SOAPHandlerChainFactory, WSGIApplication

from service.services import DummyService
 
class PlaystationNetworkAPIService(SOAPApplication):
    #factory = SOAPHandlerChainFactory
    #wsdl_content = dict(name='PlaystationNetworkAPI', targetNamespace='urn:PSN', imports=(), portType="")
 
    _wsdl = "".join(open("PlaystationNetworkAPI.wsdl").readlines())
    _noget = "".join(open("noget.html").readlines())
 
    @soapmethod(GetProfileSoapIn.typecode, GetProfileSoapOut.typecode, operation='GetProfile', soapaction='GetProfile')
    def soap_GetProfile(self, request, response, **kw):
        
        result = DummyService(response.new_GetProfileResult).GetProfile(request._psnId,request._location)
        
        response.GetProfileResult = result
        
        return request,response
    
    def _handle_GET(self, env, start_response):
        if env['QUERY_STRING'].lower() == 'wsdl':
            start_response("200 OK", [('Content-Type','text/xml')])
            return [ self._wsdl ]

        start_response("404 ERROR", [('Content-Type','text/html')])
        return [ self._noget ]
    
application = WSGIApplication()
application['PlaystationNetworkAPI'] = PlaystationNetworkAPIService()
 
def main():
  run_wsgi_app(application)
 
if __name__ == "__main__":
  main()