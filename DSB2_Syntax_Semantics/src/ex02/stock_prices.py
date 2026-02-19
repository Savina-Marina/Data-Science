def stock_prices():
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

    company = sys.argv[1]
    company_name = company.capitalize()

    if company_name not in COMPANIES:
        print("Unknown company")
        return

    value = COMPANIES[company_name]
    price = STOCKS[value]
    print(price)


if __name__ == '__main__':
    stock_prices()
