print("Welcome to tip calculator!")

bill = float(input("What was the total bill?\n"))
whatPercentage = int(input("What percentage would you like? 10%, 15%, 20%\n"))
billSplit = int(input("How many are splitting the bill?\n"))

percentageCal = float(whatPercentage / 100)
tipAmount = float(percentageCal * bill)
totalBill = float(tipAmount + bill)
billCostSplit = float(round(totalBill / billSplit, 2))


print(f"Your portion for the bill is ${billCostSplit}")