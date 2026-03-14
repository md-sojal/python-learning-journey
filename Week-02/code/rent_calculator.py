# Inputs we need from the user
# Total rent
# Total food ordeder for snacking
# Electricity spent
# How many are sharing the room
# Output = Total amount you've to pay is ...

try:
    rent = int(input("Enter your hostel/flat rent = "))
    food = int(input("Enter the amount of food ordered = "))
    electricity = int(input("Enter the amount of electricity bill = "))
    room_mates = int(input("Enter the number of persons living in hostel/flat = "))

    bill = (rent + food + electricity) / room_mates
    print(f"Your share of rent is {bill} bdt")
except ValueError:
    print("You have enterd wrong, try again")
