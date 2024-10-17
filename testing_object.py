import numpy
import matplotlib.pyplot as plt
import test_api

ticker = input("Enter the ticker: ")
test_api.get_current_stock_price(ticker)
test_api.get_fund_data(ticker)

