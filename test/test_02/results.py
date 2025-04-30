results = ["Mario", "Luigi"]

# append at the end of the list
results.append("Princess")
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")
results.append(["Bowser", "Donkey Kong Jr."])

results.remove(["Bowser", "Donkey Kong Jr."])

# add a list to the list as independent items. Otherwise, append will add a list within a list.
results.extend(["Bowser", "Donkey Kong Jr."])

results.remove("Bowser")

# insert at the specified index place
results.insert(0, "Bowser")

# will flip the list from the end to the beginning
results.reverse()
# Will print results list in one line
print(results)

# will print results in column
for name in results:
    print(name)
