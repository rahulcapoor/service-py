import six
from six.moves.urllib.parse import urlparse
import pandas as pd
NSE_INDICES = ["NIFTY 50",
               "NIFTY NEXT 50",
               "NIFTY100 LIQ 15",
               "NIFTY 100",
               "NIFTY 200",
               "NIFTY 500",
               "NIFTY MIDCAP 50",
               "NIFTY MIDCAP 100",
               "NIFTY SMALL 100",
               "NIFTY AUTO",
               "NIFTY BANK",
               "NIFTY ENERGY",
               "NIFTY FIN SERVICE",
               "NIFTY FMCG",
               "NIFTY IT",
               "NIFTY MEDIA",
               "NIFTY METAL",
               "NIFTY PHARMA",
               "NIFTY PSU BANK",
               "NIFTY REALTY",
               "NIFTY COMMODITIES",
               "NIFTY CONSUMPTION",
               "NIFTY CPSE",
               "NIFTY INFRA",
               "NIFTY MNC",
               "NIFTY PSE",
               "NIFTY SERV SECTOR",
               "NIFTY SHARIAH 25",
               "NIFTY50 SHARIAH",
               "NIFTY500 SHARIAH",
               "NIFTY100 EQUAL WEIGHT",
               "NIFTY50 USD",
               "NIFTY50 DIV POINT",
               "NIFTY DIV OPPS 50",
               "NIFTY ALPHA 50",
               "NIFTY HIGH BETA 50",
               "NIFTY LOW VOLATILITY 50",
               "NIFTY QUALITY 30",
               "NIFTY50 VALUE 20",
               "NIFTY GROWSECT 15",
               "NIFTY50 TR 2X LEV",
               "NIFTY50 TR 1X INV",               
               ]

DERIVATIVE_TO_INDEX = {"NIFTY": "NIFTY 50",
               "BANKNIFTY": "NIFTY BANK",
               "NIFTYINFRA": "NIFTY INFRA",
               "NIFTYIT": "NIFTY IT",
               "NIFTYMID50": "NIFTY MIDCAP 50",
               "NIFTYPSE": "NIFTY PSE"}

INDEX_DERIVATIVES = list(DERIVATIVE_TO_INDEX.keys())
INDEX_DERIVATIVES.append('S&P500')
INDEX_DERIVATIVES.append('DJIA')
INDEX_DERIVATIVES.append('FTSE100')

INDEX_BANK_NIFTY = {'AXISBANK':'axisbank.json',
        'BANDHANBNK':'bandhanbnk.json',
        'BANKBARODA':'bankbaroda.json',
        'FEDERALBNK':'federalbnk.json',
        'HDFCBANK':'hdfcbank.json',
        'ICICIBANK':'icicibank.json',
        'IDFCFIRSTB':'idfcfirstb.json',
        'INDUSINDBK':'indusindbk.json',
        'KOTAKBANK':'kotakbank.json',
        'PNB':'pnb.json',
        'RBLBANK':'rblbank.json',
        'SBIN':'sbin.json',
        'IGL': 'IGL.json'
        }

INDEX_NIFTY_50 = {'MARUTI':'maruti.json',
        'WIPRO':'wipro.json',
        'BHARTIARTL':'bhartiartl.json',
        'AXISBANK':'axisbank.json',
        'ZEEL':'zeel.json',
        'BRITANNIA':'britannia.json',
        'SUNPHARMA':'sunpharma.json',
        'TECHM':'techm.json',
        'ULTRACEMCO':'ultracemco.json',
        'TATASTEEL':'tatasteel.json',
        'INDUSINDBK':'indusindbk.json',
        'BAJFINANCE':'bajfinance.json',
        'UPL':'upl.json',
        'TITAN':'titan.json',
        'BPCL':'bpcl.json',
        'INFY':'infy.json',
        'GRASIM':'grasim.json',
        'ADANIPORTS':'adaniports.json',
        'SBIN':'sbin.json',
        'IOC':'ioc.json',
        'ICICIBANK':'icicibank.json',
        'JSWSTEEL':'jswsteel.json',
        'CIPLA':'cipla.json',
        'EICHERMOT':'eichermot.json',
        'HINDUNILVR':'hindunilvr.json',
        'ONGC':'ongc.json',
        'HDFC':'hdfc.json',
        'COALINDIA':'coalindia.json',
        'DRREDDY':'drreddy.json',
        'RELIANCE':'reliance.json',
        'HCLTECH':'hcltech.json',
        'ASIANPAINT':'asianpaint.json',
        'TCS':'tcs.json',
        'HDFCBANK':'hdfcbank.json',
        'KOTAKBANK':'kotakbank.json',
        'BAJAJ-AUTO':'bajaj-auto.json',
        'HINDALCO':'hindalco.json',
        'NESTLEIND':'nestleind.json',
        'LT':'lt.json',
        'ITC':'itc.json',
        'VEDL':'vedl.json',
        'TATAMOTORS':'tatamotors.json',
        'NTPC':'ntpc.json',
        'BAJAJFINSV':'bajajfinsv.json',
        'GAIL':'gail.json',
        'SHREECEM':'shreecem.json',
        'HEROMOTOCO':'heromotoco.json',
        'POWERGRID':'powergrid.json',
        'M&M':'m&m.json',
        'INFRATEL':'infratel.json',
        }

NIFTY_FNO_STOCKS = ["ACC",
"ADANIENT",
"ADANIPORTS",
"ADANIPOWER",
"AMARAJABAT",
"AMBUJACEM",
"APOLLOHOSP",
"APOLLOTYRE",
"ASHOKLEY",
"ASIANPAINT",
"AUROPHARMA",
"AXISBANK",
"BAJAJ-AUTO",
"BAJAJFINSV",
"BAJFINANCE",
"BALKRISIND",
"BANDHANBNK",
"BANKBARODA",
"BATAINDIA",
"BEL",
"BERGEPAINT",
"BHARATFORG",
"BHARTIARTL",
"BHEL",
"BIOCON",
"BOSCHLTD",
"BPCL",
"BRITANNIA",
"CADILAHC",
"CANBK",
"CENTURYTEX",
"CHOLAFIN",
"CIPLA",
"COALINDIA",
"COLPAL",
"CONCOR",
"CUMMINSIND",
"DABUR",
"DIVISLAB",
"DLF",
"DRREDDY",
"EICHERMOT",
"EQUITAS",
"ESCORTS",
"EXIDEIND",
"FEDERALBNK",
"GAIL",
"GLENMARK",
"GMRINFRA",
"GODREJCP",
"GODREJPROP",
"GRASIM",
"HAVELLS",
"HCLTECH",
"HDFC",
"HDFCBANK",
"HDFCLIFE",
"HEROMOTOCO",
"HINDALCO",
"HINDPETRO",
"HINDUNILVR",
"IBULHSGFIN",
"ICICIBANK",
"ICICIPRULI",
"IDEA",
"IDFCFIRSTB",
"IGL",
"INDIGO",
"INDUSINDBK",
"INFRATEL",
"INFY",
"IOC",
"ITC",
"JINDALSTEL",
"JSWSTEEL",
"JUBLFOOD",
"JUSTDIAL",
"KOTAKBANK",
"L&TFH",
"LICHSGFIN",
"LT",
"LUPIN",
"M&M",
"M&MFIN",
"MANAPPURAM",
"MARICO",
"MARUTI",
"MCDOWELL-N",
"MFSL",
"MGL",
"MINDTREE",
"MOTHERSUMI",
"MRF",
"MUTHOOTFIN",
"NATIONALUM",
"NAUKRI",
"NCC",
"NESTLEIND",
"NIITTECH",
"NMDC",
"NTPC",
"ONGC",
"PAGEIND",
"PEL",
"PETRONET",
"PFC",
"PIDILITIND",
"PNB",
"POWERGRID",
"PVR",
"RAMCOCEM",
"RBLBANK",
"RECLTD",
"RELIANCE",
"SAIL",
"SBILIFE",
"SBIN",
"SHREECEM",
"SIEMENS",
"SRF",
"SRTRANSFIN",
"SUNPHARMA",
"SUNTV",
"TATACHEM",
"TATACONSUM",
"TATAMOTORS",
"TATAPOWER",
"TATASTEEL",
"TCS",
"TECHM",
"TITAN",
"TORNTPHARM",
"TORNTPOWER",
"TVSMOTOR",
"UBL",
"UJJIVAN",
"ULTRACEMCO"
]

NIFTY_FNO_FILE_NAMES = {'ACC' : 'acc.json',
'ADANIENT' : 'adanient.json',
'ADANIPORTS' : 'adaniports.json',
'ADANIPOWER' : 'adanipower.json',
'AMARAJABAT' : 'amarajabat.json',
'AMBUJACEM' : 'ambujacem.json',
'APOLLOHOSP' : 'apollohosp.json',
'APOLLOTYRE' : 'apollotyre.json',
'ASHOKLEY' : 'ashokley.json',
'ASIANPAINT' : 'asianpaint.json',
'AUROPHARMA' : 'auropharma.json',
'AXISBANK' : 'axisbank.json',
'BAJAJ-AUTO' : 'bajaj-auto.json',
'BAJAJFINSV' : 'bajajfinsv.json',
'BAJFINANCE' : 'bajfinance.json',
'BALKRISIND' : 'balkrisind.json',
'BANDHANBNK' : 'bandhanbnk.json',
'BANKBARODA' : 'bankbaroda.json',
'BATAINDIA' : 'bataindia.json',
'BEL' : 'bel.json',
'BERGEPAINT' : 'bergepaint.json',
'BHARATFORG' : 'bharatforg.json',
'BHARTIARTL' : 'bhartiartl.json',
'BHEL' : 'bhel.json',
'BIOCON' : 'biocon.json',
'BOSCHLTD' : 'boschltd.json',
'BPCL' : 'bpcl.json',
'BRITANNIA' : 'britannia.json',
'CADILAHC' : 'cadilahc.json',
'CANBK' : 'canbk.json',
'CENTURYTEX' : 'centurytex.json',
'CHOLAFIN' : 'cholafin.json',
'CIPLA' : 'cipla.json',
'COALINDIA' : 'coalindia.json',
'COLPAL' : 'colpal.json',
'CONCOR' : 'concor.json',
'CUMMINSIND' : 'cumminsind.json',
'DABUR' : 'dabur.json',
'DIVISLAB' : 'divislab.json',
'DLF' : 'dlf.json',
'DRREDDY' : 'drreddy.json',
'EICHERMOT' : 'eichermot.json',
'EQUITAS' : 'equitas.json',
'ESCORTS' : 'escorts.json',
'EXIDEIND' : 'exideind.json',
'FEDERALBNK' : 'federalbnk.json',
'GAIL' : 'gail.json',
'GLENMARK' : 'glenmark.json',
'GMRINFRA' : 'gmrinfra.json',
'GODREJCP' : 'godrejcp.json',
'GODREJPROP' : 'godrejprop.json',
'GRASIM' : 'grasim.json',
'HAVELLS' : 'havells.json',
'HCLTECH' : 'hcltech.json',
'HDFC' : 'hdfc.json',
'HDFCBANK' : 'hdfcbank.json',
'HDFCLIFE' : 'hdfclife.json',
'HEROMOTOCO' : 'heromotoco.json',
'HINDALCO' : 'hindalco.json',
'HINDPETRO' : 'hindpetro.json',
'HINDUNILVR' : 'hindunilvr.json',
'IBULHSGFIN' : 'ibulhsgfin.json',
'ICICIBANK' : 'icicibank.json',
'ICICIPRULI' : 'icicipruli.json',
'IDEA' : 'idea.json',
'IDFCFIRSTB' : 'idfcfirstb.json',
'IGL' : 'igl.json',
'INDIGO' : 'indigo.json',
'INDUSINDBK' : 'indusindbk.json',
'INFRATEL' : 'infratel.json',
'INFY' : 'infy.json',
'IOC' : 'ioc.json',
'ITC' : 'itc.json',
'JINDALSTEL' : 'jindalstel.json',
'JSWSTEEL' : 'jswsteel.json',
'JUBLFOOD' : 'jublfood.json',
'JUSTDIAL' : 'justdial.json',
'KOTAKBANK' : 'kotakbank.json',
'L&TFH' : 'l&tfh.json',
'LICHSGFIN' : 'lichsgfin.json',
'LT' : 'lt.json',
'LUPIN' : 'lupin.json',
'M&M' : 'm&m.json',
'M&MFIN' : 'm&mfin.json',
'MANAPPURAM' : 'manappuram.json',
'MARICO' : 'marico.json',
'MARUTI' : 'maruti.json',
'MCDOWELL-N' : 'mcdowell-n.json',
'MFSL' : 'mfsl.json',
'MGL' : 'mgl.json',
'MINDTREE' : 'mindtree.json',
'MOTHERSUMI' : 'mothersumi.json',
'MRF' : 'mrf.json',
'MUTHOOTFIN' : 'muthootfin.json',
'NATIONALUM' : 'nationalum.json',
'NAUKRI' : 'naukri.json',
'NCC' : 'ncc.json',
'NESTLEIND' : 'nestleind.json',
'NIITTECH' : 'niittech.json',
'NMDC' : 'nmdc.json',
'NTPC' : 'ntpc.json',
'ONGC' : 'ongc.json',
'PAGEIND' : 'pageind.json',
'PEL' : 'pel.json',
'PETRONET' : 'petronet.json',
'PFC' : 'pfc.json',
'PIDILITIND' : 'pidilitind.json',
'PNB' : 'pnb.json',
'POWERGRID' : 'powergrid.json',
'PVR' : 'pvr.json',
'RAMCOCEM' : 'ramcocem.json',
'RBLBANK' : 'rblbank.json',
'RECLTD' : 'recltd.json',
'RELIANCE' : 'reliance.json',
'SAIL' : 'sail.json',
'SBILIFE' : 'sbilife.json',
'SBIN' : 'sbin.json',
'SHREECEM' : 'shreecem.json',
'SIEMENS' : 'siemens.json',
'SRF' : 'srf.json',
'SRTRANSFIN' : 'srtransfin.json',
'SUNPHARMA' : 'sunpharma.json',
'SUNTV' : 'suntv.json',
'TATACHEM' : 'tatachem.json',
'TATACONSUM' : 'tataconsum.json',
'TATAMOTORS' : 'tatamotors.json',
'TATAPOWER' : 'tatapower.json',
'TATASTEEL' : 'tatasteel.json',
'TCS' : 'tcs.json',
'TECHM' : 'techm.json',
'TITAN' : 'titan.json',
'TORNTPHARM' : 'torntpharm.json',
'TORNTPOWER' : 'torntpower.json',
'TVSMOTOR' : 'tvsmotor.json',
'UBL' : 'ubl.json',
'UJJIVAN' : 'ujjivan.json',
'ULTRACEMCO' : 'ultracemco.json',

}

NIFTY_HOLIDAY_CALENDAR = [pd.datetime(2020, 02, 21),
    pd.datetime(2020, 03, 10), 
                          pd.datetime(2020, 04, 06),
                          pd.datetime(2020, 04, 10),
                          pd.datetime(2020, 04, 14),
                          pd.datetime(2020, 05, 01),
                          pd.datetime(2020, 05, 25),
                          pd.datetime(2020, 10, 02),
                          pd.datetime(2020, 11, 16),
                          pd.datetime(2020, 11, 30),
                          pd.datetime(2020, 12, 25),
                         ]  

class URLFetch:

    def __init__(self, url, method='get', json=False, session=None,
                 headers = None, proxy = None):
        self.url = url
        self.method = method
        self.json = json

        if not session:
            self.session = requests.Session()
        else:
            self.session = session

        if headers:
            self.session.headers.update(headers)
        if proxy:
            self.update_proxy(proxy)
        else:
            self.update_proxy('')

    def set_session(self, session):
        self.session = session
        return self

    def get_session(self, session):
        self.session = session
        return self

    def __call__(self, *args, **kwargs):
        u = urlparse(self.url)
        self.session.headers.update({'Host': u.hostname})
        url = self.url%(args)
        if self.method == 'get':
            return self.session.get(url, params=kwargs, proxies = self.proxy )
        elif self.method == 'post':
            if self.json:
                return self.session.post(url, json=kwargs, proxies = self.proxy )
            else:
                return self.session.post(url, data=kwargs, proxies = self.proxy )

    def update_proxy(self, proxy):
        self.proxy = proxy
        self.session.proxies.update(self.proxy)

    def update_headers(self, headers):
        self.session.headers.update(headers)

