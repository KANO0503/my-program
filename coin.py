import yfinance as yf
import pandas as pd
from datetime import datetime

def get_bitcoin_data(period="1y"):
    """Yahoo Finance에서 비트코인 데이터를 가져옵니다."""
    btc = yf.Ticker("BTC-USD")
    data = btc.history(period=period)
    return data

def analyze_data(data):
    """비트코인 데이터를 분석하고 추천을 제공합니다."""
    # 이동 평균 계산
    data['이동_평균'] = data['Close'].rolling(window=50).mean()
    
    # 최신 가격과 이동 평균 가져오기
    latest_price = data['Close'].iloc[-1]
    moving_avg = data['이동_평균'].iloc[-1]
    
    recommendation = "유지"
    if latest_price < moving_avg:
        recommendation = "매수"
    elif latest_price > moving_avg:
        recommendation = "매도"
    
    return latest_price, moving_avg, recommendation

if __name__ == "__main__":
    period = input("분석할 기간을 입력하세요 (예: '1y'는 1년, '6mo'는 6개월): ")
    if not period:
        period = "1y"  # 기본 기간은 1년
    
    data = get_bitcoin_data(period)
    latest_price, moving_avg, recommendation = analyze_data(data)
    
    print(f"최신 비트코인 가격: ${latest_price:.2f}")
   
