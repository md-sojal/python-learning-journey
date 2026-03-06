#I did this after seeing it in a short lecture on loops in CS50 Python
def main():
    names = {"Mario", "Luigi", "Daisy", "Yoshi"}
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender):
    return f"""
    ========================================
    
    Dear {receiver},
    
    you are cordially invited to a ball at
    Peach's Castel this evening, 7:00 pm.


    Sincerely,
    {sender}

    ========================================

    """

main()
