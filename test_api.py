import yfinance as yf
import time
import requests

def get_stock_info(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    print("Stock Info:")
    print(info)

def get_stock_returns(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    returns = stock.history(period=period)['Close'].pct_change()
    print("Stock Returns:", ticker)
    print(returns)

def get_stock_history(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    history = stock.history(period=period)
    print("Stock History:", ticker)
    print(history)

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

def get_beta(ticker):
    stock = yf.Ticker(ticker)
    if 'beta' in stock.info:
        beta = stock.info['beta']
        print("Beta:")
        print(beta)
    else: 
        print("Beta not available for {ticker}")
        

# Function to get current stock price using yfinance
def get_current_stock_price(ticker):
    stock = yf.Ticker(ticker)
    
    # Get the latest stock info
    stock_info = stock.history(period='1d')
    
    # Extract the close price for the most recent day
    if not stock_info.empty:
        current_price = stock_info['Close'].iloc[-1]
        print(f"Current stock price for {ticker}: ${current_price}")
    else:
        print(f"No data available for {ticker}")

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

# Example usage
ticker = "SOXQ"

#this is just saving the calls
"""get_stock_info(ticker)
get_stock_history(ticker)
get_dividends(ticker)
get_splits(ticker)
get_actions(ticker)
get_financials(ticker)
get_balance_sheet(ticker)
get_cashflow(ticker)
get_earnings(ticker)
get_sustainability(ticker)
get_recommendations(ticker)"""""

# Continuously get stock history; only update every 11 seconds
#while True: #cntrl + c to stop
  #  get_current_stock_price(ticker)
  #  time.sleep(11)

