import sys
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from PlaystationNetworkAPI_client import *
from ZSI.twisted.wsgi import SOAPApplication, soapmethod, SOAPHandlerChainFactory, WSGIApplication
 
class PlaystationNetworkAPIService(SOAPApplication):
    #factory = SOAPHandlerChainFactory
    #wsdl_content = dict(name='PlaystationNetworkAPI', targetNamespace='urn:PSN', imports=(), portType="")
 
    #_wsdl = "".join(open("PlaystationNetworkAPI.xml").readlines())
 
    @soapmethod(GetProfileSoapIn.typecode, GetProfileSoapOut.typecode, operation='GetProfile', soapaction='GetProfile')
    def soap_GetProfile(self, request, response, **kw):
        
        GetProfileResult = response.new_GetProfileResult()
        
        GetProfileResult.Location = request._location
        GetProfileResult.PsnId = request._psnId
        GetProfileResult.AvatarSmall = "http://static-resource.np.community.playstation.net/avatar_s/WWS_J/J0003_s.png"
        GetProfileResult.Level = 4
        GetProfileResult.Progress = 16
        
        TrophyCount = GetProfileResult.new_TrophyCount()
        
        TrophyCount.Platinum = 0
        TrophyCount.Gold=0
        TrophyCount.Silver=6
        TrophyCount.Bronze=81
        TrophyCount.Total=87

        PlayedGames = GetProfileResult.new_PlayedGames()
        
        PlayedGame = PlayedGames.new_PlayedGame() 
        
        PlayedGame.Title = "Skyrim"
        
        PlayedGames.PlayedGame = [ PlayedGame ]
        
        GetProfileResult.PlayedGames = PlayedGames
        GetProfileResult.TrophyCount = TrophyCount
        response.GetProfileResult = GetProfileResult
        
        return request,response
 
application = WSGIApplication()
application['PlaystationNetworkAPI'] = PlaystationNetworkAPIService()
 
def main():
  run_wsgi_app(application)
 
if __name__ == "__main__":
  main()