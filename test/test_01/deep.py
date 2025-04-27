a = input("What is The Answer to the Great Question?")
a = a.strip().lower()

if a == "42" or a == "forty two" or a == "forty-two":
    print("Yes")
else:
    print("No")
