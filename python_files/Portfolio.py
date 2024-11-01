import api


def ssdd(): #ssdd = singular stock/etf data display
    select = input("ETF or Stock: ")
    select = select.upper()

    if select == "ETF":
        ticker = input("Enter an ETF ticker: ")
        ticker = ticker.upper()
        print(api.etf_data())
    elif select == "STOCK":
        ticker = input("Enter a stock ticker: ")
        ticker = ticker.upper()
        print(api.stock_data())
    else:
        print("Invalid selection")

def portfolio():
    tickers = [] #list of tickers in a portfolio
    weightings = [] #holdings weight in portfolio
    ipt = [] #investment per ticker
    print("Welcome to your portfolio")
    print("Please enter the tickers of your portfolio")

    while True:
        ticker = input("Enter ticker: ").upper()
        tickers.append(ticker)
        print("Portfolio: ", tickers)
        
        add = input("Would you like to add another ticker? (y/n): ").lower()
        if add != 'y':
            break

    print("Final Portfolio: ", tickers)
    book_value = float(input("Enter the book value of your portfolio: "))

    for ticker in tickers:
        weight = float(input(f"Enter the % weighting for {ticker}: "))
        weight_val = weight / 100
        weightings.append(weight_val)

    # Second loop to calculate and print amounts
    print("Investment per ticker: ", ipt)
    for ticker, weight_val in zip(tickers, weightings): #zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.<-- what the hell does that mean?
        amount = book_value * weight_val
        ipt.append(amount)
        print(ticker, ":", amount)
    print("Current Price: ")
    for ticker in tickers:
        print(ticker, ":", api.get_current_stock_price(ticker))

if __name__ == "__main__":
    print("Welcome to program")
    type_select = input("1 for singular stock/etf data display, 2 for portfolio: ")
    if type_select == "1":
        ssdd()
    elif type_select == "2":
        portfolio()
