#Python Function
from asyncio.proactor_events import _ProactorDuplexPipeTransport
from http.client import PAYMENT_REQUIRED


def add(first_number, second_number):
    total = first_number + second_number
    print("Your total is: ", total)
add(4, 5)

def scream():
    print("AAAAH!")
scream()
scream()
scream()
print("Okay, I feel much better.")

#A Definitive Buy
transaction_amount= 259.34
def process_payment():
    print(f"The total cost of this transaction will be ${transaction_amount}")
    print("Success! Payment has been processed.")
process_payment()

#Making Functions Dynamic
#Function Parameters & Data Containers

def add_numbers(numbers):
    total=sum(numbers)
    print("The sum of the numbers is:", total)
add_numbers([1,2,3,4,5])

#Function Return 
def average_numbers(numbers):
    average=(sum(numbers) / len(numbers))
    print("The average is:", average)
average_numbers([1,2,3])

def average_numbers(numbers):
    average=(sum(numbers) / len(numbers))
    return average

first_average = average_numbers([1,2,3])
second_average = average_numbers([4,5,6])
print(first_average, second_average)

#Returned Goods
weekly_claims = [5000, 1000, 8000, 10000, 3000, 3500]
def process_claims(claims):
    total_claims= sum(claims)
    total_payout= total_claims*0.30
    return total_payout

total_insurance_payout=process_claims(weekly_claims)
print(f"The total insurance payout is ${total_insurance_payout: .2f}")

#Split-Sceond Homebuying, Part 2

def price_this_home(home_price, expected_sale_price, hurdle_rate, holding_months):
    present_value = expected_sale_price / (1 + (hurdle_rate / 12)) ** holding_months
    net_present__value= present_value-home_price
    if present_value > home_price:
        print("Buy this one, junior analyst! It's worth more than it's selling for.")
    # Otherwise, take a pass:
    elif present_value < home_price:
        print("Don't buy this, as it's offered at a price higher than what it's worth.")
    # Bonus! The edge case:
    elif present_value == home_price:
        print(
            "Breakeven case! You can expect to earn exactly your hurdle rate on this deal."
        ) 
    return net_present__value

npv=price_this_home(100000, 120000, 0.10, 36)
if npv<0:
    print(f"The expected loss is ${npv: .2f}")
elif npv>0:
    print(f"The expected profit is ${npv: .2f}")
elif npv==0:
    print(f"There is neither a profit or loss")
