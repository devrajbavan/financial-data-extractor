EXCHANGE_MAP = {
    # USA
    "usa":               {"eodhd": "US",     "yahoo": ""},

    # UK
    "united kingdom":    {"eodhd": "LSE",    "yahoo": ".L"},
    "uk":                {"eodhd": "LSE",    "yahoo": ".L"},

    # Canada
    "canada":            {"eodhd": "TO",     "yahoo": ".TO"},
    "canada_neo":        {"eodhd": "NEO",    "yahoo": ".TO"},   # Yahoo merges Neo into TSX
    "canada_venture":    {"eodhd": "V",      "yahoo": ".V"},

    # Germany
    "germany_berlin":    {"eodhd": "BE",     "yahoo": ".BE"},
    "germany_hamburg":   {"eodhd": "HM",     "yahoo": ".HM"},
    "germany_xetra":     {"eodhd": "XETRA",  "yahoo": ".DE"},
    "germany_dusseldorf":{"eodhd": "DU",     "yahoo": ".DU"},
    "germany_hanover":   {"eodhd": "HA",     "yahoo": ".HA"},
    "germany_munich":    {"eodhd": "MU",     "yahoo": ".MU"},
    "germany_stuttgart": {"eodhd": "STU",    "yahoo": ".STU"},
    "germany_frankfurt": {"eodhd": "F",      "yahoo": ".F"},

    # Luxembourg
    "luxembourg":        {"eodhd": "LU",     "yahoo": None},

    # Austria
    "austria":           {"eodhd": "VI",     "yahoo": ".VI"},

    # France
    "france":            {"eodhd": "PA",     "yahoo": ".PA"},

    # Belgium
    "belgium":           {"eodhd": "BR",     "yahoo": ".BR"},

    # Spain
    "spain":             {"eodhd": "MC",     "yahoo": ".MC"},

    # Switzerland
    "switzerland":       {"eodhd": "SW",     "yahoo": ".SW"},

    # Portugal
    "portugal":          {"eodhd": "LS",     "yahoo": ".LS"},

    # Netherlands
    "netherlands":       {"eodhd": "AS",     "yahoo": ".AS"},

    # Iceland
    "iceland":           {"eodhd": "IC",     "yahoo": None},

    # Ireland
    "ireland":           {"eodhd": "IR",     "yahoo": None},

    # Finland
    "finland":           {"eodhd": "HE",     "yahoo": ".HE"},

    # Norway
    "norway":            {"eodhd": "OL",     "yahoo": ".OL"},

    # Denmark
    "denmark":           {"eodhd": "CO",     "yahoo": ".CO"},

    # Sweden
    "sweden":            {"eodhd": "ST",     "yahoo": ".ST"},

    # Czech Republic
    "czech republic":    {"eodhd": "PR",     "yahoo": None},

    # Hungary
    "hungary":           {"eodhd": "BUD",    "yahoo": None},

    # Poland
    "poland":            {"eodhd": "WAR",    "yahoo": ".WA"},

    # Greece
    "greece":            {"eodhd": "AT",     "yahoo": ".AT"},

    # Israel
    "israel":            {"eodhd": "TA",     "yahoo": ".TA"},

    # Turkey (not in your list but supported)
    "turkey":            {"eodhd": "IS",     "yahoo": ".IS"},

    # Asia
    "japan":             {"eodhd": "T",      "yahoo": ".T"},
    "hong kong":         {"eodhd": "HK",     "yahoo": ".HK"},
    "singapore":         {"eodhd": "SI",     "yahoo": ".SI"},
    "india_nse":         {"eodhd": "NSE",    "yahoo": ".NS"},
    "india_bse":         {"eodhd": "BSE",    "yahoo": ".BO"},
    "south korea":       {"eodhd": "KO",     "yahoo": ".KS"},
    "south korea_kosdaq":{"eodhd": "KQ",     "yahoo": ".KQ"},
    "taiwan":            {"eodhd": "TW",     "yahoo": ".TW"},
    "taiwan_otc":        {"eodhd": "TWO",    "yahoo": None},
    "china_shanghai":    {"eodhd": "SHG",    "yahoo": ".SS"},
    "china_shenzhen":    {"eodhd": "SHE",    "yahoo": ".SZ"},
    "indonesia":         {"eodhd": "JK",     "yahoo": ".JK"},
    "thailand":          {"eodhd": "BK",     "yahoo": ".BK"},
    "malaysia":          {"eodhd": "KLSE",   "yahoo": ".KL"},
    "philippines":       {"eodhd": "PSE",    "yahoo": None},
    "vietnam":           {"eodhd": "VN",     "yahoo": None},
    "sri lanka":         {"eodhd": "CM",     "yahoo": None},

    # Australia & NZ
    "australia":         {"eodhd": "AU",     "yahoo": ".AX"},
    "new zealand":       {"eodhd": "NZ",     "yahoo": ".NZ"},

    # Middle East
    "saudi arabia":      {"eodhd": "SR",     "yahoo": ".SR"},
    "uae":               {"eodhd": "DU",     "yahoo": ".DU"},
    "qatar":             {"eodhd": "QA",     "yahoo": ".QA"},
    "kuwait":            {"eodhd": "KW",     "yahoo": ".KW"},

    # Africa (limited Yahoo support)
    "south africa":      {"eodhd": "JSE",    "yahoo": ".JO"},
    "nigeria":           {"eodhd": "XNSA",   "yahoo": ".NG"},
    "egypt":             {"eodhd": "EGX",    "yahoo": ".CA"},
    "kenya":             {"eodhd": "XNAI",   "yahoo": None},
    "ghana":             {"eodhd": "GSE",    "yahoo": None},
    "mauritius":         {"eodhd": "SEM",    "yahoo": None},
    "morocco":           {"eodhd": "BC",     "yahoo": None},
    "uganda":            {"eodhd": "USE",    "yahoo": None},
    "zimbabwe":          {"eodhd": "VFEX",   "yahoo": None},
    "zambia":            {"eodhd": "LUSE",   "yahoo": None},
    "rwanda":            {"eodhd": "RSE",    "yahoo": None},
    "tanzania":          {"eodhd": "DSE",    "yahoo": None},
}
