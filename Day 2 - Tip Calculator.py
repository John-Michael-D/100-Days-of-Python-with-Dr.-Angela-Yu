print("Welcome to the tip calculator!")
bill = float(input("\nWhat was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

tip_amount = (tip / 100) * bill
total_cost = bill + tip_amount
print(f"\nThe total tip is: ${tip_amount:.2f}")
print(f"The total cost is: ${total_cost:.2f}")
print(f"Each person in the group of {people} should pay: ${total_cost / people:.2f}")