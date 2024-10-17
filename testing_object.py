import numpy
import test_api

def etf_data():
    test_api.get_current_stock_price(ticker)
    test_api.get_stock_history(ticker)
    test_api.get_fund_data(ticker)
    test_api.get_holdings(ticker)
    #test_api.get_beta(ticker)

def stock_data():
    test_api.get_current_stock_price(ticker)
    test_api.get_balance_sheet(ticker)
    test_api.get_cashflow(ticker)
    test_api.get_earnings(ticker)
    test_api.get_sustainability(ticker)
    test_api.get_recommendations(ticker)
    #test_api.get_beta(ticker)

select = input("ETF or Stock: ")
select = select.upper()

if select == "ETF":
    ticker = input("Enter an ETF ticker: ")
    ticker = ticker.upper()
    #ticker = "SOXQ" #manual override
    print(etf_data())
else:
    ticker = input("Enter a stock ticker: ")
    ticker = ticker.upper()
    #ticker = "NVDA" #manual override
    print(stock_data())
