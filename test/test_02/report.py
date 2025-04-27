# Shorts Dictionaries
# https://cs50.harvard.edu/python/2022/shorts/dictionaries/#dictionaries

def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft.update({"distance": "0.01", "orbit": "Sun"})
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    -----Report-----
    Name: {spacecraft.get("name")}
    Distance: {spacecraft.get("distance", "Unknown")} AU
    Orbit: {spacecraft.get("orbit", "Unknown")}
    ----------------
    """


if __name__ == '__main__':
    main()
