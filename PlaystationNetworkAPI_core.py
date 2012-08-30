from ZSI import TC

class Profile :
    def __init__(self, Location=None, PsnId=None, AvatarSmall=None, Level=0, Progress=0 ) :#, TrophyCount = None, PlayedGames = [] ):
        self.Location=Location
        self.PsnId=PsnId 
        self.AvatarSmall=AvatarSmall
        self.Level=Level
        self.Progress=Progress
#        self.TrophyCount = TrophyCount
#        self.PlayedGames = PlayedGames
        
#class TrophyCount :
#    def __init__(self, Platinum=None, ):  
        
#         public int? Platinum { get; set; }
#        public int? Gold { get; set; }
#        public int? Silver { get; set; }
#        public int? Bronze { get; set; }
#        public int? Total { get; set; }      

Profile.typecode = TC.Struct(Profile,
                             TC.String('location'),
                             TC.String('PsnId'),
                             TC.URI('AvatarSmall'),
                             TC.Integer('Level'),
                             TC.Decimal('Progress'),
                             #TC.Struct(TrophyCount),
                             'urn:PSN:Profile')                
        
