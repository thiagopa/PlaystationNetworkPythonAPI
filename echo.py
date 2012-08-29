import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from EchoServer_server import *
from ZSI.twisted.wsgi import SOAPApplication, soapmethod, SOAPHandlerChainFactory, WSGIApplication
 
class EchoService(SOAPApplication):
    factory = SOAPHandlerChainFactory
    wsdl_content = dict(name='Echo', targetNamespace='urn:echo', imports=(), portType="")
 
    @soapmethod(EchoRequest.typecode, EchoResponse.typecode, operation='Echo', soapaction='Echo')
    def soap_Echo(self, request, response, **kw):
        response = request
        return request,response
 
application = WSGIApplication()
application['echo'] = EchoService()
 
def main():
  run_wsgi_app(application)
 
if __name__ == "__main__":
  main()