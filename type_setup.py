import test_api
import testing_object as tp
import numpy

select = input("ETF or Stock: ")
select = select.upper()
#stock or etf functions

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

if select == "ETF":
    print(etf_data())

if  select == "STOCK": 
    print(stock_data())  

else:
    print("Invalid selection")
