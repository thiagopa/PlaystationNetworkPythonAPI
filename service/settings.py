# -*- coding: utf-8 -*-
## Default set of headers for requests to PSN
DEFAULT_HEADERS = {
    'User-agent':       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.19 (KHTML, like Gecko) Ubuntu/12.04 Chromium/18.0.1025.168 Chrome/18.0.1025.168 Safari/535.19',
    'Accept':           '*/*',
    'Accept-Encoding':  'gzip, deflate',
    'Accept-Language':  'pt-BR',
    'Connection':       'Keep-Alive',
}

PING_PAGE = "http://us.playstation.com/publictrophy/index.htm?onlinename=%s";
LOGIN_LANDING = "https://account.sonyentertainmentnetwork.com/external/auth/login.action?request_locale=pt_BR&service-entity=psn&returnURL=https://br.playstation.com/bruwps/PSNTicketRetrievalGenericServlet";
LOGIN_URL = "https://account.sonyentertainmentnetwork.com/external/auth/login!authenticate.action";
LOGIN_RETURN = "https://br.playstation.com/bruwps/PSNTicketRetrievalGenericServlet";
TICKET_URL = "https://us.playstation.com/uwps/PSNTicketRetrievalGenericServlet?psnAuth=true&sessionId=%s";

PSN_PROFILE = "http://us.playstation.com/playstation/psn/profiles/%s/trophies/";
PSN_GAMES = "http://us.playstation.com/playstation/psn/profile/%s/get_ordered_trophies_data";

HANDLE_URL = 'http://us.playstation.com/uwps/HandleIFrameRequests?sessionId=%s'
COOKIE_HANDLER = 'http://us.playstation.com/uwps/CookieHandler'
PORTABLE_ID = 'http://us.playstation.com/portableid/index.htm'

NO_USER_PROFILE = 'No User Profile'