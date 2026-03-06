# Pactice what i learned form cs50
# I am first defining a main function to store the return values
def main():
    x = int(input("What is the number? "))
    if is_even(x):
        print("The number is even")
    else:
        print("The number is odd")
# Now i will define how it is varified if the number is oven or odd
def is_even(n):
    return n % 2 == 0
main()