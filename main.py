import os
print("Welcome to the tip calculator!")
total_bill = int(input("What was total bill? $"))
total_tip = float(input("How much tip would you like to give? 10%, 12% or 15%?"))
amount_of_people = int(input("How many people to split the bill?"))
#calculating how to split the bill, depending on total bill size, amount of tip given and amount of people included in the bill
bill_split = round(float((total_bill/amount_of_people)*((total_tip/100)+1.0)),2)
print(f"Each person should pay: ${bill_split}")
os.system('pause')