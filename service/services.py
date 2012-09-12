#-*- coding: utf-8 -*-

from network import PSN
import logging
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from PlaystationNetworkAPI_client import *

from service import *

logger = logging.getLogger(__name__)


class Service:
    """
        Interface para os Outros Serviços
    """
    def GetProfile(self,psn_id,location):
        raise NotImplementedError( "Should have implemented this" )
    
    def GetProfileResult(self):
        return GetProfileSoapOut().new_GetProfileResult()
    
class DummyService(Service):
    """
        Serviço de testes que retorna sempre um resultado fixo
    """
    def GetProfile(self,psn_id,location):
        GetProfileResult = self.GetProfileResult()
        
        GetProfileResult.Location = location
        GetProfileResult.PsnId = psn_id
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
        
        RedDeadRedemption = PlayedGames.new_PlayedGame() 
        
        RedDeadRedemption.Id = "590951-Red-Dead-Redemption"
        RedDeadRedemption.Title = "Red Dead Redemption"
        RedDeadRedemption.Image = "http://trophy01.np.community.playstation.net/trophy/np/NPWR00867_00_3C04BB5C8E8B922C223411F0E040983D86D4B864/27D02EB3579FF13B05CB8707B7B6C79AD14C6332.PNG"
        RedDeadRedemption.Progress = 1          
        
        RedDeadRedemptionTrophyCount = RedDeadRedemption.new_TrophyCount()
        RedDeadRedemptionTrophyCount.Platinum = 0
        RedDeadRedemptionTrophyCount.Gold=0
        RedDeadRedemptionTrophyCount.Silver=0
        RedDeadRedemptionTrophyCount.Bronze=1
        RedDeadRedemptionTrophyCount.Total=1

        RedDeadRedemption.TrophyCount = RedDeadRedemptionTrophyCount

        GTAIV = PlayedGames.new_PlayedGame() 
        
        GTAIV.Id = "581447-GTA-IV"
        GTAIV.Title = "GTA IV"
        GTAIV.Image = "http://trophy01.np.community.playstation.net/trophy/np/NPWR00132_00_FB41DD6DD0A782A55D7A8497108B84EB19EDA56C/EF4A80E7CECAFBA06A2F60DA0CC3CAC53B77C9D0.PNG"
        GTAIV.Progress = 5          
        
        GTAIVTrophyCount = GTAIV.new_TrophyCount()
        GTAIVTrophyCount.Platinum = 0
        GTAIVTrophyCount.Gold=0
        GTAIVTrophyCount.Silver=0
        GTAIVTrophyCount.Bronze=5
        GTAIVTrophyCount.Total=5

        GTAIV.TrophyCount = GTAIVTrophyCount

        Rocksmith = PlayedGames.new_PlayedGame() 
        
        Rocksmith.Id = "769900-Rocksmith"
        Rocksmith.Title = "Rocksmith"
        Rocksmith.Image = "http://trophy01.np.community.playstation.net/trophy/np/NPWR02441_00_E3DD20052F61FD820B6DE55FF57DA79D2F64AA93/AB24C97C206C4154F99412E59F73A276673289F0.PNG"
        Rocksmith.Progress = 41          
        
        RocksmithTrophyCount = Rocksmith.new_TrophyCount()
        RocksmithTrophyCount.Platinum = 0
        RocksmithTrophyCount.Gold=0
        RocksmithTrophyCount.Silver=4
        RocksmithTrophyCount.Bronze=26
        RocksmithTrophyCount.Total=30

        Rocksmith.TrophyCount = RocksmithTrophyCount

        Skyrim = PlayedGames.new_PlayedGame() 
        
        Skyrim.Id = "784100-Skyrim"
        Skyrim.Title = "Skyrim"
        Skyrim.Image = "http://trophy01.np.community.playstation.net/trophy/np/NPWR02631_00_95497FBD204F38224C6536E9D88098D62FF3DA33/1A9A3826FB6B42C1B08824655A740620BC8E75F9.PNG"
        Skyrim.Progress = 49          
        
        SkyrimTrophyCount = Skyrim.new_TrophyCount()
        SkyrimTrophyCount.Platinum = 0
        SkyrimTrophyCount.Gold=0
        SkyrimTrophyCount.Silver=2
        SkyrimTrophyCount.Bronze=30
        SkyrimTrophyCount.Total=32

        Skyrim.TrophyCount = SkyrimTrophyCount
        
        DarkSouls = PlayedGames.new_PlayedGame() 
        
        DarkSouls.Id = "750900-DARK-SOULS"
        DarkSouls.Title = "DARK SOULS"
        DarkSouls.Image = "http://trophy01.np.community.playstation.net/trophy/np/NPWR00817_00_18699C4415CCDB413A543EDF44C2D40F3FB4BAC3/5D679B3A330595EE11D2AD1474548405CB6E0C79.PNG"
        DarkSouls.Progress = 5          
        
        DarkSoulsTrophyCount = DarkSouls.new_TrophyCount()
        DarkSoulsTrophyCount.Platinum = 0
        DarkSoulsTrophyCount.Gold=0
        DarkSoulsTrophyCount.Silver=0
        DarkSoulsTrophyCount.Bronze=4
        DarkSoulsTrophyCount.Total=4

        DarkSouls.TrophyCount = DarkSoulsTrophyCount

        Wanted = PlayedGames.new_PlayedGame() 
        
        Wanted.Id = "582927-Wanted"
        Wanted.Title = "Wanted"
        Wanted.Image = "http://trophy01.np.community.playstation.net/trophy/np/NPWR00512_00_80FB32B2EC373210BCE7053ED9AF0A141E9C807B/2BF34B112089BD4F3447A14B962D4022E91978F2.PNG"
        Wanted.Progress = 21          
        
        WantedTrophyCount = Wanted.new_TrophyCount()
        WantedTrophyCount.Platinum = 0
        WantedTrophyCount.Gold=0
        WantedTrophyCount.Silver=0
        WantedTrophyCount.Bronze=15
        WantedTrophyCount.Total=15

        Wanted.TrophyCount = WantedTrophyCount

        PlayedGames.PlayedGame = [ RedDeadRedemption, GTAIV, Rocksmith, Skyrim, DarkSouls, Wanted ]
        
        GetProfileResult.PlayedGames = PlayedGames
        GetProfileResult.TrophyCount = TrophyCount
        
        return GetProfileResult

     
class CrawlerService(Service):
    """
        Serviço que busca as informações do site americano
    """
    def GetProfile(self,psn_id,location):
        logger.info("Creating new GetProfileResult")
        GetProfileResult = self.GetProfileResult()
        
        logger.info("Retrieving Credentials from Database")
        psn_credential = retrieve_psn_credentials()
        
        logger.info("Input Credentials to PSN")
        psn = PSN(email=psn_credential.email, passwd=psn_credential.password)
        
        logger.info("Getting Trophies Page Parser")
        trophies = psn.trophies(psn_id)
        
        logger.debug("SOUP PRETTIFY")
        logger.debug(trophies._soup.prettify())
        
        logger.info("Parsing Profile Info")
        
        GetProfileResult.PsnId = trophies.PsnId()
        GetProfileResult.Location = location
        GetProfileResult.AvatarSmall = trophies.AvatarSmall()
        GetProfileResult.Level = trophies.Level()
        GetProfileResult.Progress = trophies.Progress()

        logger.info("Parsing Trophie Count")
        TrophyCount = GetProfileResult.new_TrophyCount()
        
        TrophyCount.Platinum = trophies.Platinum()
        TrophyCount.Gold= trophies.Gold()
        TrophyCount.Silver= trophies.Silver()
        TrophyCount.Bronze= trophies.Bronze()
        TrophyCount.Total= trophies.Total()
        
        GetProfileResult.TrophyCount = TrophyCount

        logger.info("Getting Games Page Parser")
        games = psn.games(psn_id)
        
        PlayedGames = GetProfileResult.new_PlayedGames()
        
        logger.info("Parsing Each Game Retrieved")
        for game in games :
            Game = PlayedGames.new_PlayedGame()
            
            Game.Id = game.Id()
            Game.Title = game.Title()
            Game.Image = game.Image()
            Game.Progress = game.Progress()
            
            GameTrophyCount = Game.new_TrophyCount()
            
            GameTrophyCount.Platinum = game.Platinum()
            GameTrophyCount.Gold= game.Gold()
            GameTrophyCount.Silver= game.Silver()
            GameTrophyCount.Bronze= game.Bronze()
            GameTrophyCount.Total= game.Total()
            
            Game.TrophyCount = GameTrophyCount
            
            PlayedGames.PlayedGame.append(Game)
        
        GetProfileResult.PlayedGames = PlayedGames

        return GetProfileResult
             
