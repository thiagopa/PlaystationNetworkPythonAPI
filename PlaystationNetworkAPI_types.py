##################################################
# file: PlaystationNetworkAPI_types.py
#
# schema types generated by "ZSI.generate.wsdl2python.WriteServiceModule"
#    wsdl2py --complexType PlaystationNetworkAPI.wsdl
#
##################################################

import ZSI
import ZSI.TCcompound
from ZSI.schema import LocalElementDeclaration, ElementDeclaration, TypeDefinition, GTD, GED
from ZSI.generate.pyclass import pyclass_type

##############################
# targetNamespace
# urn:PSN
##############################

class ns0:
    targetNamespace = "urn:PSN"

    class Profile_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "urn:PSN"
        type = (schema, "Profile")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.Profile_Def.schema
            TClist = [ZSI.TC.String(pname=(ns,"PsnId"), aname="_PsnId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"AvatarSmall"), aname="_AvatarSmall", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"Level"), aname="_Level", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"Progress"), aname="_Progress", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("urn:PSN","TrophyCount",lazy=False)(pname=(ns,"TrophyCount"), aname="_TrophyCount", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), GTD("urn:PSN","ArrayOfPlayedGame",lazy=False)(pname=(ns,"PlayedGames"), aname="_PlayedGames", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._PsnId = None
                    self._AvatarSmall = None
                    self._Level = None
                    self._Progress = None
                    self._TrophyCount = None
                    self._PlayedGames = None
                    return
            Holder.__name__ = "Profile_Holder"
            self.pyclass = Holder

    class TrophyCount_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "urn:PSN"
        type = (schema, "TrophyCount")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.TrophyCount_Def.schema
            TClist = [ZSI.TCnumbers.Iint(pname=(ns,"Platinum"), aname="_Platinum", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"Gold"), aname="_Gold", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"Silver"), aname="_Silver", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"Bronze"), aname="_Bronze", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), ZSI.TCnumbers.Iint(pname=(ns,"Total"), aname="_Total", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._Platinum = None
                    self._Gold = None
                    self._Silver = None
                    self._Bronze = None
                    self._Total = None
                    return
            Holder.__name__ = "TrophyCount_Holder"
            self.pyclass = Holder

    class ArrayOfPlayedGame_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "urn:PSN"
        type = (schema, "ArrayOfPlayedGame")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.ArrayOfPlayedGame_Def.schema
            TClist = [GTD("urn:PSN","PlayedGame",lazy=False)(pname=(ns,"PlayedGame"), aname="_PlayedGame", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._PlayedGame = []
                    return
            Holder.__name__ = "ArrayOfPlayedGame_Holder"
            self.pyclass = Holder

    class PlayedGame_Def(TypeDefinition):
        #complexType/complexContent extension
        schema = "urn:PSN"
        type = (schema, "PlayedGame")
        def __init__(self, pname, ofwhat=(), extend=False, restrict=False, attributes=None, **kw):
            ns = ns0.PlayedGame_Def.schema
            TClist = [ZSI.TCnumbers.Iint(pname=(ns,"Progress"), aname="_Progress", minOccurs=1, maxOccurs=1, nillable=True, typed=False, encoded=kw.get("encoded")), GTD("urn:PSN","TrophyCount",lazy=False)(pname=(ns,"TrophyCount"), aname="_TrophyCount", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            attributes = self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            if ns0.Game_Def not in ns0.PlayedGame_Def.__bases__:
                bases = list(ns0.PlayedGame_Def.__bases__)
                bases.insert(0, ns0.Game_Def)
                ns0.PlayedGame_Def.__bases__ = tuple(bases)

            ns0.Game_Def.__init__(self, pname, ofwhat=TClist, extend=True, attributes=attributes, **kw)

    class Game_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "urn:PSN"
        type = (schema, "Game")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.Game_Def.schema
            TClist = [ZSI.TC.String(pname=(ns,"Id"), aname="_Id", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"Title"), aname="_Title", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"Image"), aname="_Image", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._Id = None
                    self._Title = None
                    self._Image = None
                    return
            Holder.__name__ = "Game_Holder"
            self.pyclass = Holder

    class OnlineFriend_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "urn:PSN"
        type = (schema, "OnlineFriend")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.OnlineFriend_Def.schema
            TClist = [ZSI.TC.String(pname=(ns,"PsnId"), aname="_PsnId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"AvatarSmall"), aname="_AvatarSmall", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded")), ZSI.TC.String(pname=(ns,"Playing"), aname="_Playing", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._PsnId = None
                    self._AvatarSmall = None
                    self._Playing = None
                    return
            Holder.__name__ = "OnlineFriend_Holder"
            self.pyclass = Holder

    class ArrayOfOnlineFriends_Def(ZSI.TCcompound.ComplexType, TypeDefinition):
        schema = "urn:PSN"
        type = (schema, "ArrayOfOnlineFriends")
        def __init__(self, pname, ofwhat=(), attributes=None, extend=False, restrict=False, **kw):
            ns = ns0.ArrayOfOnlineFriends_Def.schema
            TClist = [GTD("urn:PSN","OnlineFriend",lazy=False)(pname=(ns,"OnlineFriend"), aname="_OnlineFriend", minOccurs=0, maxOccurs="unbounded", nillable=True, typed=False, encoded=kw.get("encoded"))]
            self.attribute_typecode_dict = attributes or {}
            if extend: TClist += ofwhat
            if restrict: TClist = ofwhat
            ZSI.TCcompound.ComplexType.__init__(self, None, TClist, pname=pname, inorder=0, **kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._OnlineFriend = []
                    return
            Holder.__name__ = "ArrayOfOnlineFriends_Holder"
            self.pyclass = Holder

    class GetProfile_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetProfile"
        schema = "urn:PSN"
        def __init__(self, **kw):
            ns = ns0.GetProfile_Dec.schema
            TClist = [ZSI.TC.String(pname=(ns,"psnId"), aname="_psnId", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("urn:PSN","GetProfile")
            kw["aname"] = "_GetProfile"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._psnId = None
                    return
            Holder.__name__ = "GetProfile_Holder"
            self.pyclass = Holder

    class GetProfileResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetProfileResponse"
        schema = "urn:PSN"
        def __init__(self, **kw):
            ns = ns0.GetProfileResponse_Dec.schema
            TClist = [GTD("urn:PSN","Profile",lazy=False)(pname=(ns,"GetProfileResult"), aname="_GetProfileResult", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("urn:PSN","GetProfileResponse")
            kw["aname"] = "_GetProfileResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._GetProfileResult = None
                    return
            Holder.__name__ = "GetProfileResponse_Holder"
            self.pyclass = Holder

    class Profile_Dec(ElementDeclaration):
        literal = "Profile"
        schema = "urn:PSN"
        substitutionGroup = None
        def __init__(self, **kw):
            kw["pname"] = ("urn:PSN","Profile")
            kw["aname"] = "_Profile"
            if ns0.Profile_Def not in ns0.Profile_Dec.__bases__:
                bases = list(ns0.Profile_Dec.__bases__)
                bases.insert(0, ns0.Profile_Def)
                ns0.Profile_Dec.__bases__ = tuple(bases)

            ns0.Profile_Def.__init__(self, **kw)
            if self.pyclass is not None: self.pyclass.__name__ = "Profile_Dec_Holder"

    class GetOnlineFriendsResponse_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "GetOnlineFriendsResponse"
        schema = "urn:PSN"
        def __init__(self, **kw):
            ns = ns0.GetOnlineFriendsResponse_Dec.schema
            TClist = [GTD("urn:PSN","ArrayOfOnlineFriends",lazy=False)(pname=(ns,"OnlineFriends"), aname="_OnlineFriends", minOccurs=0, maxOccurs=1, nillable=False, typed=False, encoded=kw.get("encoded"))]
            kw["pname"] = ("urn:PSN","GetOnlineFriendsResponse")
            kw["aname"] = "_GetOnlineFriendsResponse"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    self._OnlineFriends = None
                    return
            Holder.__name__ = "GetOnlineFriendsResponse_Holder"
            self.pyclass = Holder

    class emptyElement_Dec(ZSI.TCcompound.ComplexType, ElementDeclaration):
        literal = "emptyElement"
        schema = "urn:PSN"
        def __init__(self, **kw):
            ns = ns0.emptyElement_Dec.schema
            TClist = []
            kw["pname"] = ("urn:PSN","emptyElement")
            kw["aname"] = "_emptyElement"
            self.attribute_typecode_dict = {}
            ZSI.TCcompound.ComplexType.__init__(self,None,TClist,inorder=0,**kw)
            class Holder:
                __metaclass__ = pyclass_type
                typecode = self
                def __init__(self):
                    # pyclass
                    return
            Holder.__name__ = "emptyElement_Holder"
            self.pyclass = Holder

# end class ns0 (tns: urn:PSN)
