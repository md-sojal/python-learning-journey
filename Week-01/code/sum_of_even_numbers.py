# First lets create variable to store our values
total_even = 0
total_odd = 0
count = int(input("Enter your desired number "))
# Using for loop to continue until the inputed count is reached
for i in range(count):
    i += 1
# Using if condition to check weather the number is even or odd and the way to do it is by using % to only check if the remainder is 0 
    if i % 2 == 0:
        total_even += i
    else:
        total_odd += i
print(f"Sum of even numbers is {total_even}")
print(f"Sum of odd numbers is {total_odd}")