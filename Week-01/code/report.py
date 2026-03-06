# Defining main function
def main():
    spacecraft = {"name": "Voyger 1", "distance": 163}
    spacecraft.update({"distance": 0.01, "orbit": "sun"})
    print(create_report(spacecraft))
# Defining another function to call to print values
def create_report(spacecraft):
    return f"""
    ========== Report ==========
    
    Name: {spacecraft.get("name", "unknown")}      
    Distance: {spacecraft.get("distance", "unknown")} AU
    orbit: {spacecraft.get("orbit", "unknown")}
    ============================
    """
main()