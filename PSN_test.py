from PlaystationNetworkAPI_client import *
import sys, time

TRACE=None
loc = PlaystationNetworkAPILocator()
port = loc.getPlaystationNetworkAPISoap()

msg = GetProfileSoapIn()
msg._psnId = "thi_pag"
msg._location = ""
rsp = port.GetProfile(msg)
#print "PSN ID: ", rsp._PsnId
#print rsp._profile
print rsp._GetProfileResult


