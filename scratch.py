# alpha vantage key: YLHDEOH9P55Q0FJ


from alpha_vantage.timeseries import TimeSeries
import sys


def function1():
    print("First API Call Script, Returns close price of indicated ticker symbol")


function1()

ticker = str(input("Please enter ticker: \n"))
averagePrice = float(input("What is your average holding price of this company? \n"))
token = "YLHDEOH9P55Q0FJ"
time = TimeSeries(key=token, output_format='pandas')
data = time.get_daily(symbol=ticker, outputsize='compact')


print(data)
closePrice = data[0].iat[0, 3]

returnRate = round(((closePrice - averagePrice)/averagePrice) * 100, 2)
print("\nThe close price of " + ticker + " was " + str(closePrice))
print("\nYour Return Rate on " + ticker + " is " + str(returnRate)+"%")
