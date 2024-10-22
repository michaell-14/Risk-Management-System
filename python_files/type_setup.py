import api
import main
import numpy

select = input("ETF or Stock: ")
select = select.upper()
#stock or etf functions

def etf_data():
    api.get_current_stock_price(main.ticker)
    api.get_stock_history(main.ticker)
    api.get_fund_data(main.ticker)
    api.get_holdings(main.ticker)
def stock_data():
    api.get_current_stock_price(main.ticker)
    api.get_balance_sheet(main.ticker)
    api.get_cashflow(main.ticker)
    api.get_earnings(main.ticker)
    api.get_sustainability(main.ticker)
    api.get_recommendations(main.ticker)
    #test_api.get_beta(ticker)

if select == "ETF":
    print(etf_data())

if  select == "STOCK": 
    print(stock_data())  

else:
    print("Invalid selection")
