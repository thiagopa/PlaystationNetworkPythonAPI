# -*- coding: utf-8 -*-
## Default set of headers for requests to PSN
DEFAULT_HEADERS = {
    'User-agent':       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19',
    'Accept':           '*/*',
    'Accept-Encoding':  'gzip, deflate',
    'Accept-Language':  'pt-BR',
    'Connection':       'Keep-Alive',
    'X-Requested-With': 'XMLHttpRequest',
}

PING_PAGE = "http://us.playstation.com/publictrophy/index.htm?onlinename=%s";
US_LOGIN_LANDING = "https://account.sonyentertainmentnetwork.com/external/auth/login.action?request_locale=pt_BR&service-entity=psn&returnURL=https://br.playstation.com/bruwps/PSNTicketRetrievalGenericServlet";
US_LOGIN_URL = "https://account.sonyentertainmentnetwork.com/external/auth/login!authenticate.action";
US_LOGIN_RETURN = "https://br.playstation.com/bruwps/PSNTicketRetrievalGenericServlet";
TICKET_URL = "https://us.playstation.com/uwps/PSNTicketRetrievalGenericServlet?psnAuth=true&sessionId=%s";

PSN_PROFILE = "http://us.playstation.com/playstation/psn/profiles/%s/trophies/";
PSN_GAMES = "http://us.playstation.com/playstation/psn/profile/%s/get_ordered_trophies_data";

HANDLE_URL = 'http://us.playstation.com/uwps/HandleIFrameRequests?sessionId=%s'
COOKIE_HANDLER = 'http://us.playstation.com/uwps/CookieHandler?cookieName=userinfo&id=%f'
PORTABLE_ID = 'http://us.playstation.com/portableid/index.htm'

NO_USER_PROFILE = 'No User Profile'

GET_FRIENDS = "http://us.playstation.com/playstation/psn/get_friends?pscom=true&id=%f"
MY_FRIENDS = "http://us.playstation.com/myfriends/"
GET_FRIENDS_NAMES = "http://us.playstation.com/playstation/psn/profile/get_friends_names"
FRIENDS_PAGE = "http://us.playstation.com/playstation/psn/profile/friends?id=%f"
US_PLAYSTATION_COM = "http://us.playstation.com/"

UK_LOGIN_PAGE = 'https://store.playstation.com/external/index.vm?returnURL=https://secure.eu.playstation.com/sign-in/confirmation/&amp;locale=en_GB'
#UK_LOGIN_RETURN = 'https://secure.eu.playstation.com/sign-in/confirmation/&amp;locale=en_GB'
UK_LOGIN_RETURN_URL = 'https://secure.eu.playstation.com/sign-in/confirmation/'

UK_LOGIN_POST_URL = 'https://store.playstation.com/j_acegi_external_security_check?target=/external/loginDefault.action'

UK_AVATAR_URL = 'https://secure.eu.playstation.com/%s'

UK_REFERER_SESSION_ID = 'https://secure.eu.playstation.com/sign-in/confirmation/1350910716494huzdxbaf/?sessionId=%s'

PSN_PERFECT_FRIENDS_XML = "https://secure.eu.playstation.com/ajax/mypsn/friend/presence/"