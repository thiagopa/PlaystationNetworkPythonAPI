##################################################
# file: PlaystationNetworkAPI_client.py
# 
# client stubs generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#     wsdl2py -b PlaystationNetworkAPI.xml
# 
##################################################

from PlaystationNetworkAPI_types import *
import urlparse, types
from ZSI.TCcompound import ComplexType, Struct
from ZSI import client
from ZSI.schema import GED, GTD
import ZSI
from ZSI.generate.pyclass import pyclass_type

# Locator
class PlaystationNetworkAPILocator:
    PlaystationNetworkAPISoap_address = "http://localhost:8080/PlaystationNetworkAPI"
    def getPlaystationNetworkAPISoapAddress(self):
        return PlaystationNetworkAPILocator.PlaystationNetworkAPISoap_address
    def getPlaystationNetworkAPISoap(self, url=None, **kw):
        return PlaystationNetworkAPISoapSOAP(url or PlaystationNetworkAPILocator.PlaystationNetworkAPISoap_address, **kw)

# Methods
class PlaystationNetworkAPISoapSOAP:
    def __init__(self, url, **kw):
        kw.setdefault("readerclass", None)
        kw.setdefault("writerclass", None)
        # no resource properties
        self.binding = client.Binding(url=url, **kw)
        # no ws-addressing

    # op: GetProfile
    def GetProfile(self, request, **kw):
        if isinstance(request, GetProfileSoapIn) is False:
            raise TypeError, "%s incorrect request type" % (request.__class__)
        # no input wsaction
        self.binding.Send(None, None, request, soapaction="GetProfile", **kw)
        # no output wsaction
        response = self.binding.Receive(GetProfileSoapOut.typecode)
        return response

GetProfileSoapIn = GED("urn:PSN", "GetProfile").pyclass

GetProfileSoapOut = GED("urn:PSN", "GetProfileResponse").pyclass
