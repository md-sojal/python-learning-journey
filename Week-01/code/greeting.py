# I made this to try if i could take inputs in a function and get different output based on the inputs
def greet():
    user_text = input(".... ").lower()
    if "hello" in user_text:
        return "Hello there"
    elif "hi" in user_text:
        return "Hi there"
    elif "hey" in user_text:
        return "Hey there"
    else:
        return "I don't understand"
print(greet())