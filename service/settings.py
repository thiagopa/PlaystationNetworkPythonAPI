## Default set of headers for requests to PSN
DEFAULT_HEADERS = {
    'User-agent':       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)',
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