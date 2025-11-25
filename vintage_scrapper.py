import requests
import yfinance as yf
import pandas as pd

from exchange import EXCHANGE_MAP          # <-- Universal exchange file
from suffixes import YAHOO_SUFFIX_MAP      # <-- Universal suffix file


API_KEY = "API-KEY"
COUNTRY = "denmark"
MIN_REVENUE = 10_000_000


# 1) Get suffix from file
def get_suffix_for_country(country: str):
    c = country.lower().strip()
    if c not in YAHOO_SUFFIX_MAP:
        raise ValueError(f"❌ No Yahoo suffix defined for country: {country}")
    return YAHOO_SUFFIX_MAP[c]


# 2) Extract tickers from EODHD
def get_eodhd_tickers(country, api_key):
    c = country.lower()

    if c not in EXCHANGE_MAP:
        raise ValueError(f"❌ Country not found in exchange map: {country}")

    exchange_code = EXCHANGE_MAP[c]["eodhd"]

    url = f"https://eodhd.com/api/exchange-symbol-list/{exchange_code}?api_token={api_key}&fmt=json"
    r = requests.get(url)

    print("\n=== RAW EODHD RESPONSE ===")
    print("Status:", r.status_code)
    print("Body:", r.text[:300])

    try:
        data = r.json()
    except Exception:
        raise RuntimeError("❌ EODHD did NOT return JSON (rate limit / wrong exchange / invalid key).")

    tickers = []
    for item in data:
        code = item["Code"]
        # remove any ".XX"
        if "." in code:
            code = code.split(".")[0]
        tickers.append(code)

    return tickers


# 3) Validate Yahoo ticker
def get_valid_yahoo_ticker(base, country):
    suffix = get_suffix_for_country(country)
    cand = base + suffix

    t = yf.Ticker(cand)

    # If it has financials, it's a valid ticker
    try:
        if not t.financials.empty:
            return cand
    except:
        pass

    return None


# 4) Extract revenue
def get_revenue(ticker):
    t = yf.Ticker(ticker)
    try:
        df = t.financials
        if "Total Revenue" in df.index:
            return df.loc["Total Revenue"].iloc[0]
    except:
        pass
    return None


# 5) Extract final company info
def extract_required_info(ticker):
    t = yf.Ticker(ticker)
    info = t.get_info()

    return {
        "ticker": ticker,
        "name": info.get("longName") or info.get("shortName"),
        "hq_location": f"{info.get('address1', '')}, {info.get('city', '')}, "
                       f"{info.get('state', '')}, {info.get('country', '')}",
        "total_branches": info.get("fullTimeEmployees"),
        "market_cap": info.get("marketCap"),
        "current_price": info.get("currentPrice"),
        "previous_close": info.get("previousClose"),
        "volume": info.get("volume"),
        "company_description": info.get("longBusinessSummary"),
        "company_summary": info.get("longBusinessSummary"),
        "main_work": f"{info.get('sector')} — {info.get('industry')}"
    }


# MAIN
def main():
    tickers = get_eodhd_tickers(COUNTRY, API_KEY)
    print("\nRaw EODHD Tickers:", tickers)
    line = 0

    results = []

    for raw in tickers:
        try:
            print("\n---------------------------------------")
            print("Raw ticker:", raw)

            valid = get_valid_yahoo_ticker(raw, COUNTRY)
            if not valid:
                print("❌ No Yahoo match found")
                continue

            print("Yahoo ticker:", valid)

            revenue = get_revenue(valid)
            print("Revenue:", revenue)

            if not revenue or revenue < MIN_REVENUE:
                print("❌ Revenue below 10M – Skipped")
                continue

            print(f"{line}. ✔ Revenue above 10M – Extracting info...")
            info = extract_required_info(valid)
            results.append(info)
            line = line + 1

        except KeyboardInterrupt:
            print("\n⚠️ STOPPED BY USER")
            break

    df = pd.DataFrame(results)
    df.to_excel("output.xlsx", index=False)
    print("✔ Output saved to output.xlsx")
    


if __name__ == "__main__":
    main()
