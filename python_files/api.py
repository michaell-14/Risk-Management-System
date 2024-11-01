import yfinance as yf
import time
import requests

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    print("Stock Info:")
    print(info)
    return info

def get_stock_returns(ticker, period): #period = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
    stock = yf.Ticker(ticker)
    returns = stock.history(period=period)['Close'].pct_change()
    #print("Stock Returns:", ticker)
    #print(returns)
    return returns

def get_stock_history(ticker, period='1y'):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    #print("Stock History:", ticker)
    #print(history)
    return history

def get_dividends(ticker):
    stock = yf.Ticker(ticker)
    dividends = stock.dividends
    print("Dividends:")
    print(dividends)

def get_splits(ticker):
    stock = yf.Ticker(ticker)
    splits = stock.splits
    print("Stock Splits:")
    print(splits)

def get_actions(ticker):
    stock = yf.Ticker(ticker)
    actions = stock.actions
    print("Stock Actions:")
    print(actions)

def get_financials(ticker):
    stock = yf.Ticker(ticker)
    financials = stock.financials
    print("Financials:")
    print(financials)

def get_balance_sheet(ticker):
    stock = yf.Ticker(ticker)
    balance_sheet = stock.balance_sheet
    print("Balance Sheet:")
    print(balance_sheet)

def get_cashflow(ticker):
    stock = yf.Ticker(ticker)
    cashflow = stock.cashflow
    print("Cashflow:")
    print(cashflow)

def get_earnings(ticker):
    stock = yf.Ticker(ticker)
    earnings = stock.earnings
    print("Earnings:")
    print(earnings)

def get_sustainability(ticker):
    stock = yf.Ticker(ticker)
    sustainability = stock.sustainability
    print("Sustainability:")
    print(sustainability)

def get_recommendations(ticker):
    stock = yf.Ticker(ticker)
    recommendations = stock.recommendations
    print("Recommendations:")
    print(recommendations)
        

# Function to get current stock price using yfinance
def get_current_stock_price(ticker):
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period = "1d")
    current_price = stock_info["Close"].iloc[-1]
    return current_price

def get_fund_data(ticker):
    stock = yf.Ticker(ticker)
    fund_data = stock.funds_data
    assests = fund_data.asset_classes
    top_holdings = fund_data.top_holdings
    weights = fund_data.sector_weightings
    #print("Asset Classes:")
    #print(assests)
    print("Top Holdings:")
    print(top_holdings)
    print("Sector Weightings:")
    print(weights)
    
def get_holdings(ticker):
    stock = yf.Ticker(ticker)
    data = stock.funds_data
    holdings = data.equity_holdings
    print("Equity Holdings:")
    print(holdings)

#mass get function
def etf_data():
    get_current_stock_price(ticker)
    get_stock_history(ticker)
    get_fund_data(ticker)
    get_holdings(ticker)

def stock_data():
    get_current_stock_price(ticker)
    get_balance_sheet(ticker)
    get_cashflow(ticker)
    get_earnings(ticker)
    get_sustainability(ticker)
    get_recommendations(ticker)

# Example usage
ticker = "SOXQ"

#this is just saving the calls

# Continuously get stock history; only update every 11 seconds; this was found by trial and error with the yfinance API
#while True: #cntrl + c to stop
  #  get_current_stock_price(ticker)
  #  time.sleep(11)

