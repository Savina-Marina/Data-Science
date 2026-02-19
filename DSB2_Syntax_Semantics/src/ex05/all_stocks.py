def all_stocks():
    import sys

    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }

    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }

    if len(sys.argv) != 2:
        return

    raw = sys.argv[1]

    parts = raw.split(',')

    for p in parts:
        if p.strip() == '':
            return

    for p in parts:
        item = p.strip()

        ticker = item.upper()
        company = item.capitalize()

        if ticker in STOCKS:
            company_name = None
            for name, symbol in COMPANIES.items():
                if symbol == ticker:
                    company_name = name
                    break

            if company_name is None:
                print(f"{item} is an unknown company or an unknown ticker symbol")
            else:
                print(f"{ticker} is a ticker symbol for {company_name}")

        elif company in COMPANIES:
            symbol = COMPANIES[company]
            price = STOCKS[symbol]
            print(f"{company} stock price is {price}")

        else:
            print(f"{item} is an unknown company or an unknown ticker symbol")


if __name__ == "__main__":
    all_stocks()
