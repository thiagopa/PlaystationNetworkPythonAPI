import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from PlaystationNetworkAPI_client import *
from ZSI.twisted.wsgi import SOAPApplication, soapmethod, SOAPHandlerChainFactory, WSGIApplication
 
class PlaystationNetworkAPIService(SOAPApplication):
    factory = SOAPHandlerChainFactory
    wsdl_content = dict(name='PlaystationNetworkAPI', targetNamespace='urn:PSN', imports=(), portType="")
 
    _wsdl = "".join(open("wsdl/PlaystationNetworkAPI.xml").readlines())
 
    @soapmethod(GetProfileSoapIn.typecode, GetProfileSoapOut.typecode, operation='GetProfile', soapaction='GetProfile')
    def soap_GetProfile(self, request, response, **kw):
        
        #response._GetProfileResult._Profile = 
        #response._Profile = "teste"
        return request,response
 
application = WSGIApplication()
application['PlaystationNetworkAPI'] = PlaystationNetworkAPIService()
 
def main():
  run_wsgi_app(application)
 
if __name__ == "__main__":
  main()