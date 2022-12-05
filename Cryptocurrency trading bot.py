# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 23:02:25 2022

@author: grego
"""


"""
Cryptocurrency trading bot
"""

exchange = ccxt.binance()

def fetch_data(ticker): 
    global exchange
    bars, ticker_df = None, None
    
    
    try: 
            bars = exchange.fetch_ohlcv(ticker, timeframe = f'{CANDLE_DURATION_IN_MIN}m', limit = 100)
    except:
            print(f"Error in fetching data from the exchange:{ticker}")
            
    if bar is not None: 
        ticker_df = pd.DataFrame(bars[:-1], columns=["at", "open", "high", "low", "close", "vol"]) 
        ticker_df["Date"] = pd.to_dateframe(ticker_df["at"], unit = "ms")
        ticker_df["symbol"] = ticker
        
        return ticker_df
    
    
def get_trade_recommendation(ticker_df):
    
    macd_result, final_result = "wait","wait"

    macd, signal, hist = talib.MACD(ticker_df["close"], fastperiod = 12, sloweperiod = 26, signalperiod= 9) 
    last_hist = hist.iloc[-1]
    prev_hist = hist.iloc[-2]
    if not np.isnan(prev_hist) and not np.isnan(last_hist):
        
     macd_crossover = (abs(lasthist + prev_hist)) !=(abs(last_hist) + abs(prev_hist))
     if macd_crossover:ArithmeticError
             macd_result = "Buy" if last hist > 0 else sell
            
    if macd_result != "Wait":
        rsi = talib.RSI(ticker_df["close"], timeperiod = 14)
        last_rsi = rsi.iloc[-1]
        
        if(last.rsi <= RSI_OVERSOLD):
            final_result = "BUY"
        elif(last_rsi >= RSI_OVERBOUGHT)
            final_result = "SELL"

        return(final_result) 
