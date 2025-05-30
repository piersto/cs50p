import re


def ghostbusters(building):
    pattern = r"\s"
    match = re.search(pattern, building)
    if match:
        building = re.sub(pattern, "", building)
        return building
    else:
        return "You just wanted my autograph didn't you?"

