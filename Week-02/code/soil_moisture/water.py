from soil import sample

def main():
    days = 0
    moisture = sample()

    while moisture > 20:
        days += 1
        print(f"day {days}: Moisture is {moisture}%")
        moisture = sample()

    print("Time to Water!")

main()