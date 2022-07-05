#Conditional Logic: Finance
#from **** import ****


stock_price= 19.99
estimated_value= 50.99
if stock_price < estimated_value:
    print("Buy this stock because it is on sale")
else:
    print("Don't buy this stock because it is too expensive right now")

    #True & False Statements (Booleans)
    task_completed= True
    all_task_completed= False
    buy_stock= stock_price< estimated_value
    print(buy_stock)
    #Syntax for if-else statement
    is_raining= True
    if is_raining:
        print("Don't forget to bring your umbrella.")
    else:
        print("You will need your sunglasses today!")

#Double Equal Sign (Comparison Operator that Verifies)
issue_currency="USD"
price= 30.0
if issue_currency == "USD":
    print("The price is $", price)
else:
    print("The currency is not is USD")

#Compound Test (Homies Currency Requirements)
if issue_currency =="USD" and price < 40.0:
    print("The price is $", price)
else:
    print("The Currency is not in USD.")

#Write a Conditional Statement (Homies Locational Requirements)
location = "Japan"
is_registered= True
if location == "United States" and is_registered:
    print("The app for helping our less fortunate Friends")
else:
    print("Prepare to be apart of extraordinary Change")

#Multiple Conditionals
issue_currency= "EUR"
price= 30.0
if issue_currency == "USD":
    print("The currency is $", price)
elif issue_currency == "EUR":
    print("The currency is €", price )
else:
    print("The currency is not in USD or EUR.")

#Nested Conditionals
issue_currency= "USD"
if price>= 0:
    if issue_currency== "USD":
        print("The currency is $", price)
    elif issue_currency== "EUR":
        print("The currency is €", price)
    else:
        print("The currency is not in USD or Eur.")
else:   
    print( "Error, the price listed is a negative number")

#Use Nested Conditionals
ad_price = 10
company_type = "Startup"
ESP= 500
EEP= 100
if ad_price< 20:
    print("Buy this ad!")
    if company_type== "Startup":
        print("The expected profit of this company is assumed to be $", ESP )
    elif company_type== "Exsisting":
        print("The expected profit of this company is assumed to be $", EEP)
    else: 
        print("Company type is not specified")        
else:
    print("Do not buy this ad.")

#Present and Future Value
#Future Value Formula
time= 10
discount_rate= 0.10
#future_value= present_value*(1+discount_rate)^time
future_value= 1000*(1+(10/100))**10
print("$",future_value)

#Present Value Formula 
present_value= future_value/(1+discount_rate)**time
print("$", present_value)

#Split-Second Homebuying, Part 1
home_price= 115000
expected_sale_price= 130000
hurdle_rate= 0.09
#also called discount rate
holding_months= 12
present_value_e= expected_sale_price/(1+hurdle_rate/holding_months)**12
print(f"Prsent value is ${present_value_e}")
if present_value_e>home_price:
    print("The value of the home is worth more than what the seller is asking, Buy.")
elif present_value< home_price:
    print("The seller wants more money than what the house is worth, Pass.")
else:
    print("The company expects to break even on this purchase")
    