#Automation w/ Python
#Python_Iterators

from fileinput import close
import pathlib


words= ["cool!", "awesome!", "why am I shouting?"]
for word in words:
    print(word)
    print("Titlecase Word", word.title())
    print("Uppercase Word", word.upper())

#Iterators for Financial Automation
principle= 103208.56
interest_rates= [.103, .067, .099, .10]
total_interest= 0.06 
for rate in interest_rates:
    interest= rate*principle
    total_interest = total_interest + interest
    print("Your interest will be: ", interest)
print("The total interest is: ", total_interest)

#Racking Up the Profit
stock_price= 30
dividend_yields= [0.035, 0.040, 0.072, 0.012, 0.052]
total_dividend_income= 0.0
for dividends in dividend_yields:
    income= dividends*stock_price
    total_dividend_income= total_dividend_income + income
    print(f"The dividend income will be {income: .3f}")
print(f"The total dividend income is {total_dividend_income: .2f}")

#Iterating Nested Data Structures
#List of Lists
table_data_L = [
["Ticker", "Open", "Close"],
["APPL", 363.25, 363.4],
["AMZN", 2756.0, 2757.99],
["GOOG", 1409.1, 1408.2]
]

amazon_data=table_data_L[2]
amazon_opening_price=amazon_data[1]
print(amazon_opening_price)

#call data from table through combining positional index
amazon_opening_price=table_data_L[2][1]
print(amazon_opening_price)

apple_closing_price=table_data_L[1][2]
print(apple_closing_price)

for row in table_data_L:
    ticker = row[0]
    close = row[2]
    print(ticker, close)
#List of Dictionaries
table_data_D=[
{
    "Ticker": "APPL",
    "Open": 363.25,
    "Close": 363.4
},
{
    "Ticker": "AMZN",
    "Open": 2756.0,
    "Close": 2757.99
},
{
    "Ticker": "GOOG",
    "Open": 1409.1,
    "Close": 1408.2
}   
]

google_data=table_data_D[2]
print(google_data)

apple_closing_price=table_data_D[0]["Close"]
print(apple_closing_price)

for item in table_data_D:
    print(item)

for item in table_data_D:
    ticker=item["Ticker"]
    print(ticker)

#Iterating CSV Files
from pathlib import Path
my_directory= Path(".")
#"." represents the current directory
print(my_directory)

from pathlib import Path
csvpath=Path("data.csv")
print(csvpath)

#Absolute & Relative Paths
#Absolute Paths or Location Address contain full path address including folder hierarchy
#Relative Paths are the file's location relative to where you are on the computer

#Pathways to Success, Part 1
from pathlib import Path
csvpath= Path('quarterly_data.csv')
print(f"This is the relative path: {csvpath}.")
print(f"This is the absolute path:{csvpath.absolute()}")

#Read and Write to CS Files

import csv
from pathlib import Path

csvpath = Path("quarterly_data.csv")
with open(csvpath) as csvfile:
    data= csv.reader(csvfile)
    for row in data:
        print(row)

#Pathways to Success, Part 2
counter=0
with open(csvpath) as csvfile:
    data= csv.reader(csvfile)
    for row in data:
        counter= counter+1
        print (("Row Counter"), counter)
        print(row)      

#Writing CSV Files

import csv
from pathlib import Path
data=[
    {
    "first_name": "Jericho",
    "last_name": "Smith",
    "pin": 123
    },
    {
    "first_name": "Samantha",
    "last_name": "Jones",
    "pin": 456
    },
]
header=["first_name", "last_name", "pin"]
csvpath= Path("my_output.csv")
with open (csvpath, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in data:
        #using the writerow function alone converts a python list into a row of data in the CSV file 
        #values() allows computer to retrieve data from within a dictionary
        # if the data was a list of list we would use the code;
        # for row in data:
        #   csvwriter.writerow(row)
        csvwriter.writerow(row.values())
            

#Automated Equity Rounds
import csv
from pathlib import Path

equity_funding = [
    {"Company": "CryptoVisors", "Amount": 200000, "Series": "A"},
    {"Company": "Flutterwave", "Amount": 65000000, "Series": "D"},
    {"Company": "nCino", "Amount": 80000000, "Series": "D"},
    {"Company": "Privacy.com", "Amount": 10000000, "Series": "B"},
]
big_raisers=[]
for equity in equity_funding:
    if equity["Amount"]>=50000000:
        big_raisers.append(equity)
        print(big_raisers)
        
header_B= ["Company", "Amount", "Series"]
csvpath_B= Path("big_raisers.csv")
print("writing the data to a CSV file...")
with open(csvpath_B, 'w') as csvfile_B:
    csvwriter_B=csv.writer(csvfile_B, delimiter=",")
    csvwriter_B.writerow(header_B)
    for item in big_raisers:
        csvwriter_B.writerow(item.values())
        