# Algebraic Functions
from urllib.request import HTTPDefaultErrorHandler


current_price= 14.35
adjusted_price= current_price- 1.25
company_abc_stock_price= current_price
print(company_abc_stock_price)
print(current_price, adjusted_price)
print(f"The current price is: {current_price}, and the adjusted price is: {adjusted_price}")

#Hello Variable World (Stock Price Change)
Original_Price= 198.87
Current_Price= 254.32
Increase= Current_Price-Original_Price
Percent_Increase= Increase/Original_Price*100
print(Original_Price, Current_Price, Increase, Percent_Increase)

#Adding Items to Lists
tech_stocks=[]
tech_stocks.append("AAPL")
tech_stocks.append("GOOG")
tech_stocks.append("AMZN")
print(tech_stocks)

#Lists Operations
#Max
closing_prices = [12.3, 12.8, 12.54, 12.9, 12.01]
highest_closing_price = max(closing_prices)
#len (number of items in a list)
number_of_prices = len(closing_prices)
print(number_of_prices)

#Listing Assets
bank_loans = [200, 500, 900, 100, 400, 800, 100]
number_of_loans= len(bank_loans)
largest_loan_amount= max(bank_loans)
print(largest_loan_amount)
print(f"There are {number_of_loans} number of loans")

#Dictionaries
films= {
    "Nic": 105,
    "Betty": 114,
    "Dwayne": 70
}
print("Nicolas Cage Films: ", films["Nic"])
print("Betty White Films: ", films["Betty"])
print("Dwayne Johnson Films: ", films["Dwayne"])

my_stocks_dictionary= {"AAPL": 445.32, "GOOG": 1485.82}
films["Nic"]

#Dictionary Items
top_traders_per_month={}
top_traders_per_month["January"]= "Susan"
top_traders_per_month["February"]= "Samuel"
print(top_traders_per_month)
top_traders_per_month["February"]= "Harold"
print(top_traders_per_month)

#The_401K_Shuffle
accounts = {
    "Schwab": 2000, 
    "Fidelity": 8000, 
    "Merrill": 3000, 
    "Wells Fargo": 0.01
    }
del accounts["Wells Fargo"]
accounts["SoFi"]=2000
old_account_amounts = [2000, 8000, 3000, 2000]
total_amount=sum(old_account_amounts)
new_accounts={}
new_accounts["Wealthfront"]= total_amount
print(accounts["Fidelity"])
print(new_accounts)