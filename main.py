import numpy
import api


def etf_data():
    api.get_current_stock_price(ticker)
    api.get_stock_history(ticker)
    api.get_fund_data(ticker)
    api.get_holdings(ticker)
    #test_api.get_beta(ticker)

def stock_data():
    api.get_current_stock_price(ticker)
    api.get_balance_sheet(ticker)
    api.get_cashflow(ticker)
    api.get_earnings(ticker)
    api.get_sustainability(ticker)
    api.get_recommendations(ticker)
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
