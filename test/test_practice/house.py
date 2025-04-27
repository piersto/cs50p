name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    # Another way to specify it in one line
    case "Draco" | "Masha" | "Katia":
        print("Slytherin")
    # Any other text that is not specified previously -- with underline 
    case _:
        print("Who?")
