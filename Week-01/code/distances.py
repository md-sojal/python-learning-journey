distances = {
    "Voyger 1": 163,
    "Voyger 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}
"""
def main():
    for name in distances.keys():
       print(f"{name} is {distances[name ]} Au away from Earth")
"""
def main():
    for distance in distances.values():
        print(f"{distance} Au is {convert(distance)} m")

def convert(au):
    return au * 149597870700
main()