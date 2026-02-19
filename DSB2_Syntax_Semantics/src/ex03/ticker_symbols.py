import sys

def data():
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

    return COMPANIES, STOCKS


def ticker_symbols():
    if len(sys.argv) != 2:
        return

    company = sys.argv[1]

    COMPANIES, STOCKS = data()

    if company not in STOCKS:
        print("Unknown ticker")
        return

    price = STOCKS[company]

    company_name = None
    for name, value in COMPANIES.items():
        if value == company:
            company_name = name
            break

    if company_name is None:
        print("Unknown ticker")
        return

    print(company_name, price)


if __name__ == '__main__':
    ticker_symbols()
