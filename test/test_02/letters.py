def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]

    for i in range(len(names)):
        print(write_letter(names[i], "Princess"))

    for name in names:
        print(write_letter(name, "Princess"))


def write_letter(receiver, sender):
    return f"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
Hello {receiver} ! 
How are you? 

Sincerely, {sender}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""


if __name__ == '__main__':
    main()
