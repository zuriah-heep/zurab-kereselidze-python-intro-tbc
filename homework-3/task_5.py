import yfinance
from datetime import datetime

_year = int(input('Enter Bitcoin purchase year: '))
_month = int(input('Enter Bitcoin purchase month number: '))
_day = int(input('Enter Bitcoin purchase day: '))
money = float(input('Enter amount in USD you paid for Bitcoin: '))

start_date = datetime(_year, _month, _day, 1)
end_date = datetime(_year, _month, _day, 23)

bitcoin_price = yfinance.download('BTC-USD', start = start_date, end = end_date)
bitcoin_price_current = yfinance.Ticker('BTC-USD').history(period = '1d')

if money <= 0:
    print('Invalid amount in USD')
    exit(1)
elif bitcoin_price.empty:
    print('No Bitcoin data available for the date of purchase')
    exit(1)
elif bitcoin_price_current.empty:
    print('No current Bitcoin data available')
    exit(1)

bitcoin_amount = money / bitcoin_price['Close'].iloc[0]
profit = round(bitcoin_amount * bitcoin_price_current['Close'].iloc[0] - money, 2)

if profit > 0:
    print('Your profit is', profit, 'USD')
elif profit < 0:
    print('Your loss is', -profit, 'USD')
else:
    print('თხა იყიდე, თხა გაყიდე')