import numpy
import matplotlib.pyplot as plt
import test_api

ticker = input("Enter an ETF ticker: ")
#ticker = "SOXQ" #manual override
ticker = ticker.upper()


test_api.get_current_stock_price(ticker)
test_api.get_stock_history(ticker)
test_api.get_fund_data(ticker)
test_api.get_holdings(ticker)
test_api.get_beta(ticker)

